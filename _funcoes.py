import pandas as pd
import numpy as np
import csv
import os
from io import StringIO
import streamlit as st


def criar_base_dados_zerada():
    # CRIA DATAFRAME ZERADO
    arquivo = 'base_dados.csv'
    if os.path.isfile(arquivo):
        print("JÁ BASE DE DADOS CRIADA")
    else:
        colunas = ['CONTA', 'IC1', 'TIPO1', 'IC2', 'TIPO2', 'IC3', 'TIPO3', 'IC4', 'TIPO4', 'IC5', 'TIPO5', 'IC6', 'TIPO6', 'IC7', 'TIPO7',
                   'VALOR', 'TIPO_VALOR', 'NATUREZA_VALOR', 'MUNICIPIO', 'ANO', 'MES']
        df = pd.DataFrame(columns=colunas)
        df.to_csv('base_dados.csv', sep=';', index=False)
        print("BASE DE DADOS CRIADA COM SUCESSO")


def pegar_codigo_ano_mes(arquivo):
    stringio = StringIO(arquivo.getvalue().decode("utf-8"))
    string_data = stringio.readline()
    codigo = string_data.split(';')[0]
    ano = string_data.split(';')[1].split('-')[0]
    mes = string_data.split(';')[1].split('-')[1].strip()
    return codigo, ano, mes


def tratar_dataframe(arquivo, codigo, ano, mes):
    if ano == '2022':
        arquivo["IC7"] = np.nan
        arquivo["TIPO7"] = np.nan
        
    arquivo = arquivo.astype({"VALOR": 'float'})
    arquivo = arquivo.fillna(0)
    arquivo['MUNICIPIO'] = codigo
    arquivo['ANO'] = ano
    arquivo['MES'] = mes
    arquivo = arquivo[["CONTA", "IC1", "TIPO1", "IC2", "TIPO2", "IC3", "TIPO3", "IC4", "TIPO4",
                       "IC5", "TIPO5", "IC6", "TIPO6", "IC7", "TIPO7", "VALOR", "TIPO_VALOR",
                       "NATUREZA_VALOR", "MUNICIPIO", "ANO", "MES"]]
    
    st.experimental_memo.clear()
    return arquivo


def importa_cvs(arquivo):

    if validar_se_ja_existe_dataframe(codigo, ano, mes):
        print("PASSOU AKI")
        delete_dataframe(codigo, ano, mes)

    df1 = pd.read_csv(arquivo, encoding='utf-8', sep=';', skiprows=[0])
    df1 = df1.fillna(0)
    df1['IC4'] = df1['IC4'].astype(str)
    df1['MUNICIPIO'] = codigo
    df1['ANO'] = ano
    df1['MES'] = mes
    base_dados = pd.concat([base_dados, df1])
    base_dados.reset_index(inplace=True, drop=True)
    base_dados.to_csv('base_dados.csv', sep=';', index=False)
    return base_dados


def validar_se_ja_existe_dataframe(codigo, ano, mes):
    codigo_ = []
    ano_ = []
    mes_ = []
    codigo_.append(codigo)
    ano_.append(ano)
    mes_.append(mes)
    return len(base_dados[base_dados.MUNICIPIO.isin(codigo_) & base_dados.ANO.isin(ano_) & base_dados.MES.isin(mes_)]) > 0


def delete_dataframe(codigo, ano, mes):
    global base_dados
    codigo_ = []
    ano_ = []
    mes_ = []
    codigo_.append(codigo)
    ano_.append(ano)
    mes_.append(mes)
    mask = (base_dados.MUNICIPIO.isin(codigo_) &
            base_dados.ANO.isin(ano_) & base_dados.MES.isin(mes_))
    base_dados = base_dados.loc[~mask]
    return base_dados
