import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import funcoes

st.title("Análise do Arquivo MSC")
st.sidebar.header("Cidades")

uploaded_file = st.file_uploader("Escolha o arquivo MSC", accept_multiple_files=False, type=['csv'])
bytes_data = uploaded_file.read()
st.write("Nome Arquivo:", uploaded_file.name)
df = pd.read_csv(uploaded_file)
st.dataframe(df)
    