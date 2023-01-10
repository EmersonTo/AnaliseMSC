import streamlit as st
import controllers.receita.resumo as controllerReceitaResumo
import _enum as enum

funcoes_receitas = enum.enum_receitas()
enum_meses = enum.enum_mes()
enum_anos = enum.enum_anos()


def tabela_receita():
    st.title("Tabela Resumo Receita")
    with st.sidebar.form(key='PesquisarReceita'):
        funcao_receitas = st.selectbox(
            "Funções", funcoes_receitas)
        selecao_ano = st.selectbox(
            "Ano", enum_anos)
        selecao_mes = st.selectbox(
            "Mês", enum_meses)
        button_submit = st.form_submit_button("pesquisar", type="secondary")
    if button_submit:
        st.write('1702109EX')
        st.write(selecao_ano)
        st.write(selecao_mes)

        # '1702109EX'

   # tabela_receita = controllerReceitaResumo.tabela_receita(codigo, ano, mes)
