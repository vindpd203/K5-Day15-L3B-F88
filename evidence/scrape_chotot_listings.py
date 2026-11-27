"""Cào tin đăng mẫu từ Chợ Tốt API công khai (không cần auth).
Chạy: python -X utf8 evidence/scrape_chotot_listings.py [N_per_cat, mặc định 500]
Ra: evidence/raw-chotot_listings.csv
Dùng cho tool tra_gia_thi_truong: giá tham chiếu thật thay data Chợ Mẫu tự bịa.
"""
import csv, json, os, sys, time, urllib.request

N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw-chotot_listings.csv")
BATCH = 50

CATEGORIES = [
    (5010, "Điện thoại"),
    (5030, "Laptop"),
    (2020, "Xe máy"),
]

FIELDS = [
    "id", "category", "category_name", "subject", "price", "body",
    "region_name", "area_name", "account_name", "account_id", "account_oid",
    "seller_rating", "seller_sold", "num_images", "condition",
    "escrow_deposit", "mobile_model", "mobile_capacity",
]


def fetch_page(cg, offset):
    url = (f"https://gateway.chotot.com/v1/public/ad-listing"
           f"?cg={cg}&limit={BATCH}&o={offset}&st=s,k&key_param_included=true")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req, timeout=20)
    return json.loads(resp.read())


def extract(ad, cat_name):
    params = {p["id"]: p["value"] for p in ad.get("params", [])}
    return {
        "id": ad.get("ad_id", ""),
        "category": ad.get("category", ""),
        "category_name": cat_name,
        "subject": ad.get("subject", ""),
        "price": ad.get("price", ""),
        "body": (ad.get("body", "") or "")[:300],
        "region_name": ad.get("region_name", ""),
        "area_name": ad.get("area_name", ""),
        "account_name": ad.get("account_name", ""),
        "account_id": ad.get("account_id", ""),
        "account_oid": ad.get("account_oid", ""),
        "seller_rating": ad.get("average_rating", ""),
        "seller_sold": ad.get("sold_ads", ""),
        "num_images": ad.get("number_of_images", 0),
        "condition": ad.get("elt_condition", ""),
        "escrow_deposit": ad.get("escrow_can_deposit", ""),
        "mobile_model": params.get("mobile_model", ""),
        "mobile_capacity": params.get("mobile_capacity", ""),
    }


rows = []
for cg, name in CATEGORIES:
    fetched = 0
    offset = 0
    while fetched < N:
        data = fetch_page(cg, offset)
        ads = data.get("ads", [])
        if not ads:
            break
        for ad in ads:
            rows.append(extract(ad, name))
            fetched += 1
            if fetched >= N:
                break
        offset += BATCH
        time.sleep(0.3)
    print(f"  {name}: {fetched} tin")

with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print(f"Tổng: {len(rows)} tin → {OUT}")
