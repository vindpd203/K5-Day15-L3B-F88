"""Chọn mẫu và đếm review bằng thư viện chuẩn. Xem evidence/README.md."""
import argparse
import csv
import hashlib
import json
import random
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LABELS = {"bi_lua_coc", "khong_du_bang_chung", "khong_lien_quan"}
FIELDS = ["id", "stratum", "date", "score", "content", "labels", "pilot",
          "nhan_minh", "can_cu_minh", "nhan_khanh", "can_cu_khanh",
          "de_xuat_ai", "can_cu_ai", "nhan_tay", "can_cu", "nguoi_duyet", "loai_duyet"]


def read_rows(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("CSV rỗng")
    if any(not r.get("id") for r in rows) or len({r["id"] for r in rows}) != len(rows):
        raise ValueError("ID rỗng hoặc trùng")
    return rows


def normalized(text):
    return " ".join(unicodedata.normalize("NFC", text).casefold().split())


def raw_stats(rows):
    counts = Counter(k for r in rows for k in r["labels"].split("|") if k)
    years = {}
    for year in sorted({r["date"][:4] for r in rows}):
        subset = [r for r in rows if r["date"].startswith(year)]
        years[year] = {"N": len(subset), "lua_dao_keyword": sum("lua_dao" in r["labels"].split("|") for r in subset)}
    return {"N_raw": len(rows), "date_min": min(r["date"] for r in rows),
            "date_max": max(r["date"] for r in rows), "keyword_counts": dict(counts),
            "low_stars": sum(int(r["score"]) <= 2 for r in rows), "years": years}


def make_sample(rows, seed, random_n, targeted_n):
    if random_n <= 0 or targeted_n < 0:
        raise ValueError("random > 0, targeted >= 0")
    unique, seen = [], set()
    for row in rows:
        text = normalized(row["content"])
        if text and text not in seen:
            seen.add(text)
            unique.append(row)
    unique.sort(key=lambda r: r["id"])
    rng = random.Random(seed)
    base = rng.sample(unique, min(random_n, len(unique)))
    base_ids = {r["id"] for r in base}
    pool = [r for r in unique if r["id"] not in base_ids and
            {"lua_dao", "coc_chuyen_tien"} & set(r["labels"].split("|"))]
    target = rng.sample(pool, min(targeted_n, len(pool)))
    if not base:
        raise ValueError("Không có nội dung hợp lệ")
    queue = []
    for stratum, group in (("random", base), ("keyword", target)):
        for row in group:
            record = {field: "" for field in FIELDS}
            record.update({k: row[k] for k in ("id", "date", "score", "content", "labels")})
            record.update(stratum=stratum, pilot="0")
            queue.append(record)
    pilot = set()
    for stratum in ("random", "keyword"):
        group = [r for r in queue if r["stratum"] == stratum]
        pilot.update(r["id"] for r in rng.sample(group, min(15, len(group))))
    rest = [r for r in queue if r["id"] not in pilot]
    pilot.update(r["id"] for r in rng.sample(rest, min(30 - len(pilot), len(rest))))
    for row in queue:
        row["pilot"] = str(int(row["id"] in pilot))
    return queue, {"seed": seed, "N_unique_nonempty": len(unique),
                   "excluded_empty_or_duplicate": len(rows) - len(unique),
                   "random_requested": random_n, "keyword_requested": targeted_n,
                   "random_selected": len(base), "keyword_selected": len(target),
                   "keyword_pool_after_random": len(pool), "pilot": len(pilot)}


def count_labels(rows):
    # Bản nhãn công khai (annotations-codex.csv) bỏ bớt cột; cột thiếu coi như rỗng.
    rows = [{**dict.fromkeys(FIELDS, ""), **r} for r in rows]
    result = {}
    for row in rows:
        if row["stratum"] not in {"random", "keyword"} or row["pilot"] not in {"0", "1"}:
            raise ValueError("Tầng mẫu hoặc pilot không hợp lệ")
        for field in ("nhan_minh", "nhan_khanh", "nhan_tay"):
            if row[field] and row[field] not in LABELS:
                raise ValueError(f"{row['id']}: nhãn sai tại {field}")
        for label, reason in (("nhan_minh", "can_cu_minh"), ("nhan_khanh", "can_cu_khanh")):
            if row[label] and not row[reason].strip():
                raise ValueError(f"{row['id']}: thiếu căn cứ cho {label}")
        if row["nhan_tay"] and (not row["can_cu"].strip() or not row["nguoi_duyet"].strip()):
            raise ValueError(f"{row['id']}: thiếu căn cứ hoặc người duyệt nhãn cuối")
        if row["nhan_tay"] and row.get("loai_duyet") not in {"ai", "human"}:
            raise ValueError(f"{row['id']}: cần loai_duyet = ai hoặc human")
        if row.get("loai_duyet") == "human" and row["nguoi_duyet"].strip().casefold() == "codex":
            raise ValueError(f"{row['id']}: Codex phải được khai là ai, không phải human")
    for group in ("random", "keyword"):
        subset = [r for r in rows if r["stratum"] == group]
        reviewed = [r for r in subset if r["nhan_tay"]]
        counts = Counter(r["nhan_tay"] for r in reviewed)
        complete = bool(subset) and len(reviewed) == len(subset)
        result[group] = {"selected": len(subset), "reviewed": len(reviewed),
                         "human_reviewed": sum(r["loai_duyet"] == "human" for r in reviewed),
                         "ai_reviewed": sum(r["loai_duyet"] == "ai" for r in reviewed),
                         "pending": len(subset) - len(reviewed),
                         "labels": {label: counts[label] for label in sorted(LABELS)},
                         "complete": complete,
                         "bi_lua_coc_percent": round(100 * counts["bi_lua_coc"] / len(subset), 2) if complete else None}
    pilot = [r for r in rows if r["pilot"] == "1"]
    pairs = [r for r in pilot if r["nhan_minh"] and r["nhan_khanh"]]
    return {"strata": result, "pilot_selected": len(pilot), "pilot_paired": len(pairs),
            "minh_labeled": sum(bool(r["nhan_minh"]) for r in rows),
            "khanh_labeled": sum(bool(r["nhan_khanh"]) for r in rows),
            "pilot_minh_labeled": sum(bool(r["nhan_minh"]) for r in pilot),
            "pilot_khanh_labeled": sum(bool(r["nhan_khanh"]) for r in pilot),
            "pilot_agree": sum(r["nhan_minh"] == r["nhan_khanh"] for r in pairs),
            "ai_suggested": sum(bool(r["de_xuat_ai"]) for r in rows),
            "note": "loai_duyet ghi nguồn duyệt cuối; nguồn gợi ý ban đầu và cách xác nhận ghi trong manifest. Nhãn Minh xác nhận qua chat không đồng nghĩa có đối chiếu độc lập Minh/Khánh. Không tính tỷ lệ gộp; chưa đủ nhãn cuối thì % = null."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sample = sub.add_parser("sample")
    sample.add_argument("raw", type=Path)
    sample.add_argument("--seed", type=int, default=20261127)
    sample.add_argument("--random", type=int, default=300)
    sample.add_argument("--targeted", type=int, default=500)
    sample.add_argument("--name", default="sample")
    count = sub.add_parser("count")
    count.add_argument("csv", type=Path)
    stats = sub.add_parser("stats")
    stats.add_argument("raw", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "count":
            rows = read_rows(args.csv)
            manifest_path = args.csv.with_suffix(".json")
            if not manifest_path.exists():
                raise ValueError("Cần manifest .json từ lệnh sample để kiểm mẫu số gốc")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            original = {(r["id"], r["stratum"], r["pilot"]) for r in manifest["selected_ids"]}
            current = {(r["id"], r["stratum"], r["pilot"]) for r in rows}
            if original != current or len(rows) != len(manifest["selected_ids"]):
                raise ValueError("Mẫu đã bị thêm/bớt ID, đổi tầng hoặc pilot so với manifest")
            report = count_labels(rows)
        elif args.command == "stats":
            report = raw_stats(read_rows(args.raw))
            report["sha256"] = hashlib.sha256(args.raw.read_bytes()).hexdigest()
        else:
            if not args.name or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in args.name):
                raise ValueError("--name chỉ gồm chữ, số, dấu - và _")
            queue, report = make_sample(read_rows(args.raw), args.seed, args.random, args.targeted)
            report["raw_sha256"] = hashlib.sha256(args.raw.read_bytes()).hexdigest()
            out = ROOT / "private" / args.name
            out.parent.mkdir(exist_ok=True)
            paths = [out.with_suffix(s) for s in (".csv", ".json", ".pilot.csv")]
            if any(p.exists() for p in paths):
                raise ValueError("Mẫu đã tồn tại; không ghi đè nhãn, hãy dùng --name khác")
            for path, subset in ((paths[0], queue), (paths[2], [r for r in queue if r["pilot"] == "1"])):
                with path.open("x", encoding="utf-8-sig", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=FIELDS)
                    writer.writeheader()
                    writer.writerows(subset)
            report["selected_ids"] = [{"id": r["id"], "stratum": r["stratum"], "pilot": r["pilot"]} for r in queue]
            paths[1].write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
            report = {k: v for k, v in report.items() if k != "selected_ids"}
            report.update(sample_file=str(paths[0]), pilot_file=str(paths[2]))
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Lỗi: {error}\n")


if __name__ == "__main__":
    main()
