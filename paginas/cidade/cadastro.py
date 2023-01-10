import streamlit as st
import controllers.cidade as controllerCidade
import models.cidade as cidade


def criar():
    st.title("Cadastro de Cidade")
    with st.form(key="incluir_cidade", clear_on_submit=True):
        input_nome = st.text_input(label="Nome Cidade *", placeholder="Cidade")
        input_codigo_siconfi = st.text_input(
            label="Código Siconfi", placeholder="Código")
        input_button_submit = st.form_submit_button("Salvar", type="secondary")
    if input_button_submit:
        if input_nome == '':
            st.error('Preencha o Nome da Cidade', icon="🚨")
        else:
            controllerCidade.Incluir(cidade.Cidade(
                input_nome, input_codigo_siconfi))
            st.success("Cidade Incluido com Sucesso!")
            input_nome = ''
