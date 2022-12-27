import streamlit as st
import pandas as pd
import numpy as np
import csv
import os

st.title("Análise do Arquivo MSC")
st.sidebar.header("Cidades")

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
