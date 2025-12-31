import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename= "logs/ingestion_db.log",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_df(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con= engine, if_exists= 'replace', index= False)

def load_raw_data():
    '''This function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        df = pd.read_csv('data/'+file)
        logging.info(f"Ingesting: {file} in db")
        ingest_df(df, file[:-4], engine)
    end= time.time()
    total_time = (end - start)/60
    logging.info("------------Ingestion Complete----------------")
    logging.info(f'\n Total time taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()    