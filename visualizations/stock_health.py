# visualizations/stock_health.py
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("📈 Loading transformed inventory data...")
    df = pd.read_parquet("data/processed/inventory_transformed.parquet")

    # Stock health summary
    stock_summary = df.groupby("category")["stock"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    plt.bar(stock_summary.index, stock_summary.values)
    plt.title("Total Stock by Category")
    plt.xlabel("Category")
    plt.ylabel("Units in Stock")
    plt.tight_layout()
    plt.show()

    # Reorder analysis
    reorder_summary = df.groupby("category")["needs_reorder"].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    plt.bar(reorder_summary.index, reorder_summary.values * 100)
    plt.title("Reorder Rate by Category (%)")
    plt.xlabel("Category")
    plt.ylabel("% of Products Needing Reorder")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
