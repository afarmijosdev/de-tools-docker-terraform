#!/usr/bin/env python
# coding: utf-8



import pandas as pd
from tqdm.auto import tqdm
from sqlalchemy import create_engine
import click






@click.command()
@click.option('--db-user', default='root', show_default=True, help='Database user')
@click.option('--db-password', default='root', show_default=True, help='Database password')
@click.option('--db-server', default='localhost', show_default=True, help='Database server/host')
@click.option('--db-port', default=5432, type=int, show_default=True, help='Database port')
@click.option('--db-name', default='ny_taxi', show_default=True, help='Database name')
@click.option('--db-table', 'db_tableName', default='yellow_taxi_trips', show_default=True, help='Target table name')
@click.option('--db-zone-table', 'db_zone_tableName', default='zones', show_default=True, help='Target zone table name')
@click.option('--year', default=2021, type=int, show_default=True, help='Year of the dataset')
@click.option('--month', default=1, type=int, show_default=True, help='Month of the dataset')
def main(db_user, db_password, db_server, db_port, db_name, db_tableName, db_zone_tableName, year, month):

    #url_tripData = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_{year}-{month:02d}.csv.gz'
    url_tripData=f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month:02d}.parquet'
    url_zoneData=f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
    print(f'url_tripData:{url_tripData}')
    print(f'url_zoneData:{url_zoneData}')
    print(f'Db Info: Server: {db_server} Port: {db_port} DB: {db_name} Table: {db_tableName}')

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}')
    #df = pd.read_parquet(url_tripData)
    df = pd.read_parquet(url_tripData)

    df.head(n=0).to_sql(name=db_tableName, con=engine, if_exists='replace')
    df.to_sql(name=db_tableName, con=engine, if_exists='append')

    print("Inserted on Data Trip:", len(df))

    var_dtype = {
        "LocationID": "Int64",
        "Borough": "string",
        "Zone": "string",
        "service_zone": "string"
    }

    df_zones = pd.read_csv(url_zoneData, dtype=var_dtype)
    df_zones.head(n=0).to_sql(name=db_zone_tableName, con=engine, if_exists='replace')
    df_zones.to_sql(name=db_zone_tableName, con=engine, if_exists='append')

    print("Inserted on Data Zones:", len(df_zones))

if __name__ == '__main__':
    main()

#df = pd.read_csv(url_tripData, compression="gzip", dtype=var_dtype,    parse_dates=var_parse_dates)






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




