import services.database as db
import models.cidade as cidade
import streamlit as st


def Incluir(cidade):
    cursor = db.conn.cursor()
    print("*********AKI", cidade.nome, cidade.codigo_siconfi)
    cursor.execute("""INSERT INTO public.cidade(nome, codigo_siconfi) VALUES ('%s','%s');"""
                   % (cidade.nome, cidade.codigo_siconfi))
    print("AKI**************", cidade.nome, cidade.codigo_siconfi)

    db.conn.commit()
    