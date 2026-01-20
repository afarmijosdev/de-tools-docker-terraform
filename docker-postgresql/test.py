import pandas as pd

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


df = pd.read_csv(url, compression="gzip")

print(df.head())