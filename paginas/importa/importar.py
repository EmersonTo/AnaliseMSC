import streamlit as st
import pandas as pd
import _funcoes as funcoes
import controllers.msc as controllerMsc
import models.msc as msc


def importar_arquivo():
    uploaded_file = st.file_uploader(
        "Escolha o arquivo MSC",  type=['csv'])
    if uploaded_file is not None:
        detalhes = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
        codigo, ano, mes = funcoes.pegar_codigo_ano_mes(uploaded_file)
        df = pd.read_csv(uploaded_file, encoding='utf-8',
                         sep=';', skiprows=[0], dtype=str)
        df = funcoes.tratar_dataframe(df, codigo, ano, mes)
        st.dataframe(df.style.format({'VALOR': '{:.2f}'}))
        controllerMsc.Excluir(codigo, ano, mes)
        st.success('Registro Anteriores Excluído com Sucesso no Banco de Dados')
        for index, row in df.iterrows():
            controllerMsc.Incluir(msc.Msc(row["CONTA"], row["IC1"], row["TIPO1"], row["IC2"], row["TIPO2"],
                                          row["IC3"], row["TIPO3"], row["IC4"], row["TIPO4"], row["IC5"], row["TIPO5"], row["IC6"],
                                          row["TIPO6"], row["IC7"], row["TIPO7"], row["VALOR"], row["TIPO_VALOR"], row["NATUREZA_VALOR"],
                                          row["MUNICIPIO"], row["ANO"], row["MES"]))
        st.success('Registro Importado no Banco de Dados com Sucesso')
