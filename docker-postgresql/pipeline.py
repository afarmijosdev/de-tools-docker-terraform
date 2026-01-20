import subprocess

print(f'print the pip version')

# Run command and capture output as text
result = subprocess.run(["pip", "--version"], capture_output=True, text=True)

# Access the output and error
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return Code:", result.returncode)

print(f'Other task ------------ ')

import sys
print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())
df.to_parquet(f"output_day_{sys.argv[1]}.parquet")


