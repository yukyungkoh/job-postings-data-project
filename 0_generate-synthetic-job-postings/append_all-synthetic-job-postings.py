import pandas as pd
import glob
import os

# Set the directory where your CSV files are stored
data_dir = "data"
output_file = os.path.join(data_dir, "synthetic_job_postings_combined.csv")

# Get all matching CSV files
csv_files = sorted(glob.glob(os.path.join(data_dir, "synthetic_job_posting_*.csv")))

# Exclude the combined file if it already exists
csv_files = [f for f in csv_files if not f.endswith("synthetic_job_postings_combined.csv")]

# Read and append all CSVs
combined_df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)

# Save to a single CSV
combined_df.to_csv(output_file, index=False)

print(f"✅ Combined {len(csv_files)} files. Output saved to: {output_file}")