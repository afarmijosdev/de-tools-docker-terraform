#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from tqdm.auto import tqdm
from sqlalchemy import create_engine


db_user='root'
db_password='root'
db_server='localhost'
db_port=5432
db_name='ny_taxi'
db_tableName='yellow_taxi_trips'



year = 2021
month = 1

url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_{year}-{month:02d}.csv.gz'


var_dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

var_parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

#df = pd.read_csv(url, compression="gzip", dtype=var_dtype,    parse_dates=var_parse_dates)

print('New structure: ')
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}')

df_iter = pd.read_csv(url, compression="gzip", dtype=var_dtype,
    parse_dates=var_parse_dates,iterator=True, chunksize=200000)

first = True

for df_chunk in tqdm(df_iter):

    if first:
        # Create table schema (no data)
        df_chunk.head(0).to_sql(
            name=db_tableName,
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_chunk.to_sql(
        name=db_tableName,
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_chunk))





# In[31]:


#df.head()


# In[32]:


#df.dtypes


# In[33]:


#df.shape


# In[34]:


#len(df)


# In[35]:


#df['tpep_pickup_datetime']


# In[36]:


#get_ipython().system('uv add sqlalchemy psycopg2-binary')


# In[38]:






# In[40]:


#df.head(0)


# In[39]:


#print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[41]:


#df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# In[57]:





# In[47]:


#for df_chunk in df_iter:
#    print(len(df_chunk))


# In[48]:


#get_ipython().system('uv add tdqm')


# In[58]:





# In[59]:




# In[ ]:




