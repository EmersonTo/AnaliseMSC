import psycopg2
import streamlit as st


@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.


@st.experimental_memo
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

@st.experimental_memo
def run_insert(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()

@st.experimental_memo
def run_delete(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()
