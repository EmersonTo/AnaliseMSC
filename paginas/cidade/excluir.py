import streamlit as st
import controllers.cidade as controllerCidade
import models.cidade as cidade
import pandas as pd


def excluir():

    st.title("Excluir Cidade")

    excluir_id = st.number_input(label="Insira o ID", format="%d", step=1)
    col1, col2 = st.columns(2)
    with col1:
        button_excluir_select = st.button('Consultar')
    with col2:
        button_delete = st.button('Excluir', type='primary')
    if button_excluir_select:
        row = controllerCidade.Consulta_id(excluir_id)
        if len(row) == 0:
            st.error('ID não localizado', icon="🚨")
        else:
            df = pd.DataFrame(row, columns=(
                "ID", "Nome", "Código Siconfi"))
            df = df.set_index("ID")
            st.dataframe(df)

    if button_delete:
        controllerCidade.Excluir(excluir_id)
        st.success('Registro Excluído com Sucesso')
