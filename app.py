import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import funcoes

st.title("Análise do Arquivo MSC")
st.sidebar.header("Cidades")

uploaded_files = st.file_uploader(
    "Escolha o arquivo MSC", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Nome Arquivo:", uploaded_file.name)
    funcoes.importa_base_dados(uploaded_file)
    