import services.database as db
import streamlit as st


def tabela_receita(codigo, ano, mes):
    rows = db.run_query("""SELECT ic3, sum(previsto), sum(previsao_atualizada), sum(receita_arrecadada)  from 
                (SELECT ic3, sum(valor) as previsto, 0 as previsao_atualizada, 0 as receita_arrecadada
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes <= '%s'
                    and conta =  '521110000' and tipo_valor = 'ending_balance'
                    group by 1
                    
                union all

                SELECT ic3, 0 as previsto, sum(valor) as previsao_atualizada, 0 as receita_arrecadada
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes <= '%s'
                    and conta in ('521110000',' 521200000') and tipo_valor = 'ending_balance'
                    group by 1
                    
                union all

                SELECT ic3, 0 as previsto, 0 as previsao_atualizada, sum(valor) as receita_arrecadada
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes <= '%s'
                    and conta in (' 621200000',' 621300000') and tipo_valor = 'ending_balance'
                    group by 1) tab_receita
                group by 1""" % (codigo,ano,mes,codigo,ano,mes,codigo,ano,mes))

    return rows
