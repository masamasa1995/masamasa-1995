import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


st.title('ネイル棚卸')

connection_config = {
    'user':'postgres',
    'password':'postgres',
    'host':'192.168.0.15',
    'port':'5432',
    'database':'postgres',
}

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))
df = pd.read_sql(sql='select *  from mt_equipment', con=engine)
df
