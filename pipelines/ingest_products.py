# pipelines/ingest_products.py
import pandas as pd
from pathlib import Path

def main():
    print("📥 Reading raw product and inventory data...")
    products = pd.read_csv("data/data-raw/products.csv")
    inventory = pd.read_csv("data/data-raw/inventory.csv")

    print("🔗 Merging datasets...")
    merged = pd.merge(products, inventory, on="product_id", how="left")

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    merged.to_parquet("data/processed/products_inventory.parquet", index=False)

    print(f"✅ Saved merged data to data/processed/products_inventory.parquet ({len(merged)} rows)")

if __name__ == "__main__":
    main()
