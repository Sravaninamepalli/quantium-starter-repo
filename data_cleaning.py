import pandas as pd
import glob
import os

# -----------------------------
# Step 1: Locate CSV files
# -----------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "data")

csv_files = glob.glob(os.path.join(data_dir, "*.csv"))

print("Found CSV files:", csv_files)

# -----------------------------
# Step 2: Read and combine CSVs
# -----------------------------
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# -----------------------------
# Step 3: Filter only Pink Morsels
# -----------------------------
data = data[data["product"] == "pink morsel"]

# -----------------------------
# Step 4: Clean price column
# -----------------------------
data["price"] = data["price"].str.replace("$", "", regex=False).astype(float)

# -----------------------------
# Step 5: Create sales column
# -----------------------------
data["sales"] = data["price"] * data["quantity"]

# -----------------------------
# Step 6: Select required fields
# -----------------------------
final_df = data[["sales", "date", "region"]]

# -----------------------------
# Step 7: Save final output
# -----------------------------
output_path = os.path.join(script_dir, "pink_morsel_sales.csv")
final_df.to_csv(output_path, index=False)

print("Task 2 complete. Output saved as pink_morsel_sales.csv")
print("Final shape:", final_df.shape)
