"""Kiểm tính tái lập, mẫu số, nhãn AI và nhãn thiếu căn cứ."""
import unittest
import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from count import count_labels, make_sample, raw_stats


def fixture(n=50):
    return [{"id": f"T{i:03d}", "date": "2026-11-01", "score": "1",
             "content": f"synthetic test content {i}", "labels": "lua_dao" if i % 2 else ""}
            for i in range(n)]


class EvidenceTests(unittest.TestCase):
    def test_sample_reproducible_and_disjoint(self):
        rows = fixture()
        first, meta = make_sample(rows, 20261127, 20, 500)
        self.assertEqual((first, meta), make_sample(rows, 20261127, 20, 500))
        self.assertEqual(len(first), len({r["id"] for r in first}))
        self.assertEqual(sum(r["pilot"] == "1" for r in first), 30)
        self.assertEqual(meta["keyword_selected"], meta["keyword_pool_after_random"])
        self.assertEqual(meta["random_selected"], 20)

    def test_normalized_duplicates_removed(self):
        rows = fixture(1)
        rows += [{**rows[0], "id": "T999", "content": "  SYNTHETIC TEST CONTENT 0  "}]
        queue, meta = make_sample(rows, 1, 300, 500)
        self.assertEqual(len(queue), 1)
        self.assertEqual(meta["excluded_empty_or_duplicate"], 1)

    def test_ai_does_not_count_as_human_review(self):
        queue, _ = make_sample(fixture(2), 1, 2, 0)
        for row in queue:
            row["de_xuat_ai"] = "bi_lua_coc"
        report = count_labels(queue)
        self.assertEqual(report["strata"]["random"]["reviewed"], 0)
        self.assertIsNone(report["strata"]["random"]["bi_lua_coc_percent"])
        self.assertEqual(report["ai_suggested"], 2)

    def test_review_requires_reason_and_reviewer(self):
        queue, _ = make_sample(fixture(2), 1, 2, 0)
        queue[0]["nhan_tay"] = "bi_lua_coc"
        with self.assertRaises(ValueError):
            count_labels(queue)
        queue[0].update(can_cu="synthetic test reason", nguoi_duyet="test", loai_duyet="human")
        report = count_labels(queue)
        self.assertIsNone(report["strata"]["random"]["bi_lua_coc_percent"])
        queue[1].update(nhan_tay="khong_lien_quan", can_cu="synthetic test", nguoi_duyet="test", loai_duyet="human")
        self.assertEqual(count_labels(queue)["strata"]["random"]["bi_lua_coc_percent"], 50)

    def test_invalid_label_rejected(self):
        queue, _ = make_sample(fixture(2), 1, 2, 0)
        queue[0]["nhan_minh"] = "not-a-label"
        with self.assertRaises(ValueError):
            count_labels(queue)

    def test_codex_final_labels_are_not_human_reviews(self):
        queue, _ = make_sample(fixture(2), 1, 2, 0)
        for row in queue:
            row.update(nhan_tay="khong_lien_quan", can_cu="synthetic test", nguoi_duyet="Codex", loai_duyet="ai")
        report = count_labels(queue)
        self.assertEqual(report["strata"]["random"]["reviewed"], 2)
        self.assertEqual(report["strata"]["random"]["human_reviewed"], 0)
        self.assertEqual(report["strata"]["random"]["ai_reviewed"], 2)
        self.assertEqual(report["pilot_paired"], 0)
        queue[0]["loai_duyet"] = "human"
        with self.assertRaises(ValueError):
            count_labels(queue)

    def test_minh_confirmation_does_not_create_khanh_review(self):
        queue, _ = make_sample(fixture(2), 1, 2, 0)
        for row in queue:
            row.update(nhan_minh="khong_lien_quan", can_cu_minh="Confirmed in test",
                       nhan_tay="khong_lien_quan", can_cu="Test reason",
                       nguoi_duyet="Nguyễn Nhật Minh", loai_duyet="human")
        report = count_labels(queue)
        self.assertEqual(report["minh_labeled"], 2)
        self.assertEqual(report["strata"]["random"]["human_reviewed"], 2)
        self.assertEqual(report["khanh_labeled"], 0)
        self.assertEqual(report["pilot_paired"], 0)

    def test_stats_keep_raw_denominator(self):
        rows = fixture(4)
        rows[1]["content"] = rows[0]["content"]
        report = raw_stats(rows)
        self.assertEqual(report["N_raw"], 4)
        self.assertEqual(report["keyword_counts"]["lua_dao"], 2)

    def test_cli_rejects_removed_sample_row(self):
        queue, _ = make_sample(fixture(3), 1, 3, 0)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            with path.open("w", encoding="utf-8-sig", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(queue[0]))
                writer.writeheader()
                writer.writerows(queue[:-1])
            path.with_suffix(".json").write_text(json.dumps({"selected_ids": [
                {k: r[k] for k in ("id", "stratum", "pilot")} for r in queue
            ]}), encoding="utf-8")
            process = subprocess.run([sys.executable, "-X", "utf8",
                                      str(Path(__file__).with_name("count.py")), "count", str(path)],
                                     capture_output=True, encoding="utf-8")
            self.assertEqual(process.returncode, 1)
            self.assertIn("manifest", process.stderr)


if __name__ == "__main__":
    unittest.main()
