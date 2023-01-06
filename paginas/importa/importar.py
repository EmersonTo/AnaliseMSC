import streamlit as st
import pandas as pd
import _funcoes as funcoes
import csv
from io import StringIO


def importar_arquivo():
    uploaded_file = st.file_uploader(
        "Escolha o arquivo MSC",  type=['csv'])
    if uploaded_file is not None:
        detalhes = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
        st.write(uploaded_file)
        #dataframe = pd.read_csv(uploaded_file, encoding='utf-8', sep=';')
        # st.dataframe(dataframe)
        #df = funcoes.importa_cvs(uploaded_file)
        #bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.readline()
        st.write(string_data)
        print(type(string_data))
        codigo = (str(string_data[0]).strip('[]').split(';'))[0].strip("'")
        ano = ((str(string_data[0]).strip('[]').split(';'))
               [1]).strip('[]').split('-')[0]
        mes = ((str(string_data[0]).strip('[]').split(';'))[
               1]).strip('[]').split('-')[1].strip("'")
        st.write(codigo)
        st.write(ano)
        st.write(mes)
