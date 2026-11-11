# File: README.md

# Kisumu Fish Market Association Sales Analysis 
A SQL query script that connects to the sales database and prints summary with key metrics.
It analyzes the first three months of digital sales records for a county government sponsor report. 

## What It Does

- Connects to the database
- Returns a summary report of Kisumu fish sales data, indicating top three vendors per sales generation, profitability per buyer type and total monthly revenue 
- Plots a bar chart for visual representation of total monthly revenue and saves it as PNG file


## Usage

Run the program from the project's folder where the database file(ksm_fish_sales.db) is saved. 
```
python ksm_fish_sales.py
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
DB_PATH = Path(__file__).parent / "ksm_fish_sales.db"

queries = { }

for title, sql in queries.items():
            df = pd.read_sql_query(sql, conn)
            print(f"\n{title}")
            print("-" * len(title))
            print(df.to_string(index=False))

```

## Sample Output

```
2. Profitability per buyer_type
-------------------------------
buyer_type  sales  total_kg  avg_price_per_kg
    retail     59     826.3             405.0
 wholesale     31    2041.6             355.0

```

## Stack

Python Pandans, SQL, Matplotlib


## Pricing Note
This analysis would cost KES 120000 at a consulting firm. I will charge KES 65000 to conduct this analysis over 8 working days. 