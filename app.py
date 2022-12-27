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
    detalhes = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
    dataframe = pd.read_csv(uploaded_file, encoding='utf-8',sep=';')
    st.dataframe(dataframe)


    