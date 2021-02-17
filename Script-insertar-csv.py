import pandas as pd
from pyspark import SparkFiles
from sqlalchemy import create_engine

class insert():
    def insert_client(self):
        df = pd.read_csv ('client_table.csv')
        print(df)
        engine = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df in pd.read_csv("client_table.csv",chunksize=30000):
            i = 0
            j = 0
            df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
            df.index += j
            i+=1
            df.to_sql('client_table.csv',engine, index=False, if_exists='append')
            j = df.index[-1] + 1
   

    def insert_driver(self):
        df2 = pd.read_csv ('driver_table.csv')
        print(df2)
        engine2 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df2 in pd.read_csv("driver_table.csv",chunksize=1000):
            i = 0
            j = 0
            df2 = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
            df.index += j
            i+=1
            df2.to_sql('driver_table.csv',engine2, index=False, if_exists='append')
            j = df2.index[-1] + 1
            
    def insert_reservation(self):
        df3 = pd.read_csv('reservation_table.csv')
        print(df3)
        engine3 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df3 in pd.read_csv('reservation_table.csv', chunksize=3106171):
             i = 0
             j = 0
             df3 = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
             df.index += j
             i+=1
            
            df3.to_sql('reservation_table.csv',engine3,index=False,if_exists='append')
             j = df3.index[-1] + 1
            
    def insert_trip(self):
        df4 = pd.read_csv('trip_table.csv')
        print(df4)
        engine4 = create_engine('postgresql://urbvan:root2022@database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres')
        for df4 in pd.read_csv('trip_table.csv',chunksize=175292):
             i = 0
             j = 0
             df4 = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
             df4.index += j
             i+=1
            df4.to_sql('trip_table.csv',engine4,index=False,if_exists='append')
            j = df4.index[-1] + 1
    def insert_with_spark(self):
        myData = spark.read.format("csv").option("header","true").load("client_table.csv")
        url = 'postgresql:database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com
        myData.write.format('jdbc').options(
            
            url='jdbc:%s' % url,
            driver='org.postgresql.Driver',
            dbtable='client',
            user='urbvan',
             password='').mode('append').save()
        
