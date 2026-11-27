"""Cào profile người bán từ Chợ Tốt API công khai, dựa trên account_oid trong raw-chotot_listings.csv.
Chạy: python -X utf8 evidence/scrape_chotot_sellers.py
Ra: evidence/raw-chotot_sellers.csv
Dùng cho tool kiem_tin_dang: tuổi tài khoản và tên người bán của tin Chợ Tốt (kiem_tai_khoan là danh sách cảnh báo, không dùng file này).
"""
import csv, json, os, sys, time, urllib.request
from datetime import datetime

DIR = os.path.dirname(os.path.abspath(__file__))
LISTINGS = os.path.join(DIR, "raw-chotot_listings.csv")
OUT = os.path.join(DIR, "raw-chotot_sellers.csv")

FIELDS = [
    "account_id", "account_oid", "full_name", "create_date", "account_age_days",
    "phone_verified", "email_verified", "zalo_verified", "is_active", "address",
]


def fetch_profile(oid):
    url = f"https://gateway.chotot.com/v1/public/profile/{oid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=15)
    return json.loads(resp.read())


with open(LISTINGS, encoding="utf-8-sig") as f:
    listings = list(csv.DictReader(f))
oids = list({r["account_oid"]: r["account_id"] for r in listings if r["account_oid"]})
unique = {r["account_oid"]: r["account_id"] for r in listings if r["account_oid"]}
print(f"{len(unique)} sellers to fetch")

now = datetime.now()
rows = []
errors = 0
for i, oid in enumerate(unique):
    try:
        p = fetch_profile(oid)
        ct = p.get("create_time") or p.get("start_time")
        create_dt = datetime.fromtimestamp(ct) if ct else None
        rows.append({
            "account_id": p.get("account_id", ""),
            "account_oid": oid,
            "full_name": p.get("full_name", ""),
            "create_date": create_dt.strftime("%Y-%m-%d") if create_dt else "",
            "account_age_days": (now - create_dt).days if create_dt else "",
            "phone_verified": p.get("phone_verified", ""),
            "email_verified": p.get("email_verified", ""),
            "zalo_verified": "t" if p.get("zalo_id") == "verified" else "f",
            "is_active": p.get("is_active", ""),
            "address": p.get("address", ""),
        })
    except Exception as e:
        errors += 1
    if (i + 1) % 100 == 0:
        print(f"  {i+1}/{len(unique)} done, {errors} errors")
    time.sleep(0.2)

with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print(f"Tổng: {len(rows)} sellers ({errors} errors) → {OUT}")
