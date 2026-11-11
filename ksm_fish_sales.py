import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

#db must sit in the same folder as this script
DB_PATH = Path(__file__).parent / "ksm_fish_sales.db"

queries =  {
"1. Top three vendors per revenue generation":"""
    SELECT
        vendor_name,
        SUM(dIly_total_kes) AS total_revenue
    FROM ksm_fish_sales
    GROUP BY vendor_name
    ORDER BY total_revenue DESC
    LIMIT 3;
    """,
"2. Profitability per buyer_type": """    
    SELECT
        buyer_type,
        COUNT(*) AS sales,
        ROUND(SUM(kg_sold), 1) AS total_kg,
        ROUND(SUM(dIly_total_kes) / SUM(kg_sold), 0) AS avg_price_per_kg
    FROM ksm_fish_sales
    GROUP BY buyer_type
    ORDER BY avg_price_per_kg DESC;
    """,
"3. Total monthly revenue":  """

    SELECT
        strftime('%Y-%m', date) AS month,
        COUNT (*) AS sales,
        ROUND(SUM(dIly_total_kes), 0) AS total_revenue
    FROM ksm_fish_sales
    GROUP BY month
    ORDER BY month;
    """,
}


def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        for title, sql in queries.items():
            df = pd.read_sql_query(sql, conn)
            print(f"\n{title}")
            print("-" * len(title))
            print(df.to_string(index=False))
    
        df = pd.read_sql_query(sql, conn)
        plt.bar(df["month"], df["total_revenue"], color="#1F4E79")
        plt.title("Monthly Revenue, Kisumu Fish Market (KES)")
        plt.ylabel("Revenue (KES)")
        plt.tight_layout()
        plt.savefig("ksm_monthly_revenue.png", dpi=150)
    
    finally:
        conn.close()

if __name__ == "__main__":
    main()
