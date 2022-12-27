import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import funcoes

st.title("Análise do Arquivo MSC")
st.sidebar.header("Cidades")

uploaded_file = st.file_uploader("Escolha o arquivo MSC",  type=['csv'])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    