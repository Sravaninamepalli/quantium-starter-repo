from pathlib import Path
import pandas as pd
import sys

script_dir = Path(__file__).resolve().parent   # directory where the script lives
data_dir = script_dir / "data"                  # adjust if your data folder is somewhere else

print("Script directory:", script_dir)
print("Looking for CSVs in:", data_dir)

if not data_dir.exists():
    print("Data directory does not exist:", data_dir)
    sys.exit(1)

csv_files = sorted(data_dir.glob("*.csv"))
print("Found CSV files:", [str(p.name) for p in csv_files])

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {data_dir}. Check path and working directory.")

dfs = []
for p in csv_files:
    try:
        df = pd.read_csv(p, parse_dates=["date"])  # parse_dates optional
        print(f"Read {p.name} -> shape: {df.shape}")
        dfs.append(df)
    except Exception as e:
        print(f"Failed to read {p}: {e}")

if not dfs:
    raise ValueError("No dataframes were read successfully; nothing to concatenate.")

all_data = pd.concat(dfs, ignore_index=True)
print("Concatenated dataframe shape:", all_data.shape)