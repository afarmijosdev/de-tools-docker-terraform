import pandas as pd

#url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
url='https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'

df = pd.read_parquet(url)

print(df.head())