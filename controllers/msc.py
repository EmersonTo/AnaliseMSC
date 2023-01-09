import services.database as db
import models.msc as msc
import streamlit as st


def Incluir(msc):
    db.run_insert("""INSERT INTO public.msc(
	                conta, ic1, tipo1, ic2, tipo2, ic3, tipo3, ic4, tipo4, ic5, 
                    tipo5, ic6, tipo6, ic7, tipo7, valor, tipo_valor, natureza_valor, 
                    codigo_siconfi, ano, mes)
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 
                        '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"""
                  % (msc.conta, msc.ic1, msc.tipo1, msc.ic2, msc.tipo2, msc.ic3, msc.tipo3,
                     msc.ic4, msc.tipo4, msc.ic5, msc.tipo5, msc.ic6, msc.tipo6, msc.ic7,
                     msc.tipo7, msc.valor, msc.tipo_valor, msc.natureza_valor, msc.codigo_siconfi,
                     msc.ano, msc.mes))


def Excluir(codigo, ano, mes):
    row = db.run_delete("""DELETE FROM public.msc where codigo_siconfi = '%s' and ano = '%s' 
                            and mes = '%s'"""
                        % (codigo, ano, mes))
