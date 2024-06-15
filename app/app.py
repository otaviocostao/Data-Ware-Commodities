import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Carregar as variaveis do arquivo .env
load_dotenv()

# Obter as variaveis do arquivo .env
DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Url de conexão com o banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

def get_data():
    query = f"""
    SELECT 
        *
    FROM
        public.dm_commodities;
    """

    df = pd.read_sql(query, engine)
    return df

st.set_page_config(page_title='Dashboard de Commodities', layout='wide')

st.title('Dashboard de Commodities')

st.write("""
Este Dashboard mostra o dado de commodities e suas transações.
""")

df = get_data()

st.dataframe(df)
