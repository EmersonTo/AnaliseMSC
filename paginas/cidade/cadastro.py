import streamlit as st
import controllers.cidade as controllerCidade
import models.cidade as cidade


def criar():
    st.title("Cadastro de Cidade")
    with st.form(key="incluir_cidade"):
        input_nome = st.text_input(label="Nome Cidade")
        input_codigo_siconfi = st.text_input(
            label="Código Siconfi")
        input_button_submit = st.form_submit_button("Salvar", type="secondary")
    if input_button_submit:
        controllerCidade.Incluir(cidade.Cidade(input_nome,input_codigo_siconfi))
        st.success("Cidade incluido com sucesso!")
