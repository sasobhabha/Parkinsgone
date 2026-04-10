import json
import pandas as pd
from tqdm import tqdm

rows = []

with open("data/raw/data.txt", "r", encoding="utf-8") as f:
    for line in tqdm(f, desc="Processing OFF foods"):
        try:
            item = json.loads(line)
        except:
            continue

        nutr = item.get("nutriments", {})
        categories = (item.get("categories", "") or "").lower()

        rows.append({
            "food": item.get("product_name", ""),
            "brand": item.get("brands", ""),
            "categories": item.get("categories", ""),
            "tyrosine_mg": nutr.get("tyrosine_100g", 0),
            "phenylalanine_mg": nutr.get("phenylalanine_100g", 0),
            "fiber_g": nutr.get("fiber_100g", 0),
            "protein_g": nutr.get("proteins_100g", 0),
            "carbs_g": nutr.get("carbohydrates_100g", 0),
            "fat_g": nutr.get("fat_100g", 0),

            "polyphenol_flag": int(any(x in categories for x in [
                "cocoa", "chocolate", "berry", "tea", "coffee"
            ])),

            "fermented_flag": int(any(x in categories for x in [
                "yogurt", "kimchi", "kefir", "sauerkraut", "miso", "tempeh", "fermented"
            ]))
        })

df = pd.DataFrame(rows)
df.to_csv("data/processed/off_features.csv", index=False)
print("Saved data/processed/off_features.csv")

