import services.database as db
import models.cidade as cidade
import streamlit as st


def Incluir(cidade):
    db.run_insert("""INSERT INTO public.cidade(nome, codigo_siconfi) VALUES ('%s','%s');"""
                  % (cidade.nome, cidade.codigo_siconfi))


def Consulta_id(id):
    row = db.run_query("""SELECT id,nome,codigo_siconfi FROM public.cidade where id = '%s'"""
                       % (id))
    st.experimental_memo.clear()
    return row


def Excluir(id):
    row = db.run_delete("""DELETE FROM public.cidade where id = '%s'"""
                        % (id))
