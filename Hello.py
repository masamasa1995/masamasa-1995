import streamlit as st
import numpy as np
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


st.title('ネイル棚卸')

conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM mt_equipment;', ttl="10m")

for row in df.itertuples():
    st.write(f"{row.equip_nm}")
