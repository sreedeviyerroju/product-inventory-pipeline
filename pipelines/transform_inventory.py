# pipelines/transform_inventory.py
import pandas as pd
from pathlib import Path

def main():
    print("🔧 Transforming product + inventory data...")
    df = pd.read_parquet("data/processed/products_inventory.parquet")

    # Simulate daily sales rate (rough estimate)
    df["daily_sales_estimate"] = (df["stock"] + df["on_order"]) / 30
    df["days_of_stock_left"] = df["stock"] / df["daily_sales_estimate"]
    df["needs_reorder"] = df["stock"] < df["reorder_level"]

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df.to_parquet("data/processed/inventory_transformed.parquet", index=False)

    print(f"✅ Transformed data saved to data/processed/inventory_transformed.parquet ({len(df)} rows)")

if __name__ == "__main__":
    main()
