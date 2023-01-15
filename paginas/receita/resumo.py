import streamlit as st
import controllers.receita.resumo as controllerReceitaResumo
import _enum as enum
import controllers.geral.codigo_cidade as codigoCidade
import pandas as pd

funcoes_receitas = enum.enum_receitas()
enum_meses = enum.enum_mes()
enum_anos = enum.enum_anos()
enum_nivel = enum.enum_receitas_nivel()


def tabela_receita():
    cidade_lista = enum.enum_cidade()

    with st.sidebar.form(key='PesquisarReceita'):
        funcao_receitas = st.selectbox(
            "Funções", funcoes_receitas)
        selecao_cidade = st.selectbox(
            "Município", cidade_lista)
        selecao_ano = st.selectbox(
            "Ano", enum_anos)
        selecao_mes = st.selectbox(
            "Mês", enum_meses)
        if funcao_receitas == "Resumo por Nível":
            selecao_nivel = st.selectbox(
                "Nível", enum_nivel)
        button_submit = st.form_submit_button("pesquisar", type="secondary")

    if button_submit:
        if funcao_receitas == "Resumo":
            st.title("Tabela Resumo Receita")
            codigo_cidade = str(codigoCidade.retorna_codigo_cidade(
                selecao_cidade)).strip("[('',)]")

            if not codigo_cidade:
                st.error('Código da Cidade não Encontrado', icon="🚨")

            else:
                st.markdown(
                    f"Município: :green[{selecao_cidade}] Ano: :green[{selecao_ano}] Mês: :green[{selecao_mes}]")
                resumoReceita = controllerReceitaResumo.tabela_receita(
                    codigo_cidade, selecao_ano, selecao_mes)

                df = pd.DataFrame(resumoReceita, columns=(
                    'Receita', 'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

                # Inject CSS with Markdown
                st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

                # Display an interactive table
                st.table(df.style.format(
                    {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))

        if funcao_receitas == "Resumo por Receita/Fonte":
            st.title("Tabela Resumo Receita por Fonte")
            codigo_cidade = str(codigoCidade.retorna_codigo_cidade(
                selecao_cidade)).strip("[('',)]")

            if not codigo_cidade:
                st.error('Código da Cidade não Encontrado', icon="🚨")

            else:
                st.markdown(
                    f"Município: :green[{selecao_cidade}] Ano: :green[{selecao_ano}] Mês: :green[{selecao_mes}]")
                resumoReceita = controllerReceitaResumo.tabela_receita_por_fonte(
                    codigo_cidade, selecao_ano, selecao_mes)

                df = pd.DataFrame(resumoReceita, columns=(
                    'Receita', 'Fonte', 'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

                # Inject CSS with Markdown
                st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

                # Display an interactive table
                st.table(df.style.format(
                    {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))

        if funcao_receitas == "Resumo por Nível":
            st.title("Tabela Resumo Receita por Nível")
            codigo_cidade = str(codigoCidade.retorna_codigo_cidade(
                selecao_cidade)).strip("[('',)]")

            if not codigo_cidade:
                st.error('Código da Cidade não Encontrado', icon="🚨")
            else:
                st.markdown(
                    f"Município: :green[{selecao_cidade}] Ano: :green[{selecao_ano}] Mês: :green[{selecao_mes}] Nível: :green[{selecao_nivel}]")
                if selecao_nivel == 'Geral':
                    resumoReceitaNivelGeral = controllerReceitaResumo.tabela_receita_nivel_geral(
                        codigo_cidade, selecao_ano, selecao_mes)

                    df = pd.DataFrame(resumoReceitaNivelGeral, columns=(
                        'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """

                    # Inject CSS with Markdown
                    st.markdown(hide_dataframe_row_index,
                                unsafe_allow_html=True)

                    # Display an interactive table
                    st.table(df.style.format(
                        {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))

                elif selecao_nivel < '5':
                    resumoReceitaNivel = controllerReceitaResumo.tabela_receita_nivel(
                        selecao_nivel, codigo_cidade, selecao_ano, selecao_mes)

                    df = pd.DataFrame(resumoReceitaNivel, columns=(
                        'Contas', 'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """

                    # Inject CSS with Markdown
                    st.markdown(hide_dataframe_row_index,
                                unsafe_allow_html=True)

                    # Display an interactive table
                    st.table(df.style.format(
                        {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))
                else:

                    nivel = int(selecao_nivel) + 1
                    resumoReceitaNivel = controllerReceitaResumo.tabela_receita_nivel(
                        nivel, codigo_cidade, selecao_ano, selecao_mes)

                    df = pd.DataFrame(resumoReceitaNivel, columns=(
                        'Contas', 'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                    hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """

                    # Inject CSS with Markdown
                    st.markdown(hide_dataframe_row_index,
                                unsafe_allow_html=True)

                    # Display an interactive table
                    st.table(df.style.format(
                        {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))

        if funcao_receitas == "Resumo por Fonte":
            st.title("Tabela Resumo por Fonte")
            codigo_cidade = str(codigoCidade.retorna_codigo_cidade(
                selecao_cidade)).strip("[('',)]")

            if not codigo_cidade:
                st.error('Código da Cidade não Encontrado', icon="🚨")

            else:
                st.markdown(
                    f"Município: :green[{selecao_cidade}] Ano: :green[{selecao_ano}] Mês: :green[{selecao_mes}]")
                resumoFonte = controllerReceitaResumo.tabela_fonte(
                    codigo_cidade, selecao_ano, selecao_mes)

                df = pd.DataFrame(resumoFonte, columns=(
                    'Fonte', 'Previsão', 'Atualizada', 'Arrecadado Até Mês'))

                hide_dataframe_row_index = """
                <style>
                .row_heading.level0 {display:none}
                .blank {display:none}
                </style>
                """

                # Inject CSS with Markdown
                st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

                # Display an interactive table
                st.table(df.style.format(
                    {'Arrecadado Até Mês': '{:.2f}', 'Atualizada': '{:.2f}', 'Previsão': '{:.2f}'}))
