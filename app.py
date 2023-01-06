import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import _funcoes as funcoes
import services.database as db
import _enum as enum
import paginas.cidade.cadastro as pgCadastroCidade
import paginas.cidade.excluir as pgExcluirCidade
import paginas.importa.importar as pgImportar

telas = enum.enum_telas()
funcionalidades = enum.enum_funcionalidadeas()
cidade_lista = enum.enum_cidade()


st.sidebar.header("Menu")
selecao = st.sidebar.selectbox("Telas", telas)

if selecao == "Cidade":
    funcionalidades = st.sidebar.selectbox("Funções", funcionalidades)
    if funcionalidades == "Cadastrar":
        pgCadastroCidade.criar()
    if funcionalidades == "Excluir":
        pgExcluirCidade.excluir()


else:
    if selecao == "Importar Arquivo":
        st.subheader("IMPORTAR ARQUIVO")
        pgImportar.importar_arquivo()

    elif selecao == "Receita":
        st.subheader("RECEITA")
        data = pd.read_csv("base_dados.csv")
        st.dataframe(data)

    elif selecao == "Despesa":
        st.subheader("DESPESA")
        rows = db.run_query("SELECT nome from cidade;")
