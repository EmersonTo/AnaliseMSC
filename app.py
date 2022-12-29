import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import _funcoes as funcoes
import services.database as db
import _enum as enum
import paginas.cidade.cadastro as pgCadastroCidade




telas = enum.enum_telas()
funcionalidades = enum.enum_funcionalidadeas()
cidade_lista = enum.enum_cidade()


st.sidebar.header("Menu")
selecao = st.sidebar.selectbox("Telas",telas)

if selecao == "Cidade":
    funcionalidades = st.sidebar.selectbox("Funções",funcionalidades)
    if funcionalidades == "Cadastrar":
        pgCadastroCidade.criar()
        

else:
    municipio = st.sidebar.selectbox("Munícipio",cidade_lista)

    if selecao == "Importar Arquivo":
        st.subheader("IMPORTAR ARQUIVO")
        uploaded_file = st.file_uploader("Escolha o arquivo MSC",  type=['csv'])
        if uploaded_file is not None:
            detalhes = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
            dataframe = pd.read_csv(uploaded_file, encoding='utf-8',sep=';')
            st.dataframe(dataframe)
        
    elif selecao == "Receita":
        st.subheader("RECEITA")
        data = pd.read_csv("base_dados.csv")
        st.dataframe(data)

    elif selecao == "Despesa":
        st.subheader("DESPESA")
        rows = db.run_query("SELECT nome from cidade;")






    