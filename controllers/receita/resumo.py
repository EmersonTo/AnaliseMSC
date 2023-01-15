import services.database as db
import streamlit as st


def tabela_receita(codigo, ano, mes):
    rows = db.run_query("""select 
                                case when conta is null then 'TOTAL GERAL' else conta end,
                                previsto, previsao_atualizada , receita_arrecadada  from 
                            (SELECT 
                                ic4 as conta, 
                                sum(previsto) as previsto, 
                                sum(previsao_atualizada) as previsao_atualizada, 
                                sum(receita_arrecadada) as receita_arrecadada  
                            from 
                                (SELECT ic4, (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsto, 
                                    0 as previsao_atualizada, 
                                    0 as receita_arrecadada
                                    ,natureza_valor
                                    FROM public.msc
                                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                                    and conta::text like  '5211%%%%' and tipo_valor = 'ending_balance'
                                    group by 1,5
                                    
                                union all

                                SELECT ic4, 0 as previsto, 
                                    (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsao_atualizada,
                                    0 as receita_arrecadada,natureza_valor
                                    FROM public.msc
                                    
                                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                                    and conta::text similar to '(5211|5212)%%%%' and tipo_valor = 'ending_balance'
                                    group by 1,5
                                    
                                union all

                                SELECT ic4, 0 as previsto, 0 as previsao_atualizada, 
                                    (case when natureza_valor = 'C' then sum(valor) else  sum(valor)*-1 end) as receita_arrecadada
                                    ,natureza_valor
                                    FROM public.msc
                                    
                                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                                    and conta in ('621200000','621300000') and tipo_valor = 'ending_balance'
                                    group by 1,5) tab_receita
                                group by rollup (1)
                                order by 1 ) as tab""" % (codigo, ano, mes, codigo, ano, mes, codigo, ano, mes))
    st.experimental_memo.clear()
    return rows


def tabela_receita_por_fonte(codigo, ano, mes):
    rows = db.run_query("""select 
                                case when conta is null then 'TOTAL GERAL' else conta end as conta,
                                case when fonte is null then ' ' else fonte end as fonte,
                                previsto,
                                previsao_atualizada,
                                receita_arrecadada 
                            from 
                        (SELECT ic4 as conta ,ic2 as fonte, sum(previsto) as previsto, sum(previsao_atualizada) as previsao_atualizada, sum(receita_arrecadada) as receita_arrecadada   from 
                        
                        (SELECT ic4,ic2, (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsto, 
                            0 as previsao_atualizada, 0 as receita_arrecadada,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text like  '5211%%%%' and tipo_valor = 'ending_balance'
                    group by 1,2,6
                    
                union all

                SELECT ic4,ic2, 0 as previsto, 
                    (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsao_atualizada, 
                    0 as receita_arrecadada,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text similar to '(5211|5212)%%%%' and tipo_valor = 'ending_balance'
                    group by 1,2,6
                    
                union all

                SELECT ic4,ic2, 0 as previsto, 0 as previsao_atualizada, 
                    (case when natureza_valor = 'C' then sum(valor) else  sum(valor)*-1 end) as receita_arrecadada
                    ,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta in ('621200000','621300000') and tipo_valor = 'ending_balance'
                    group by 1,2,6) tab_receita
                group by rollup (1 ,2)
				order by 1,2) as tab
            where (conta is not null and fonte is not null) or (conta is null and fonte is null)
                """ % (codigo, ano, mes, codigo, ano, mes, codigo, ano, mes))
    st.experimental_memo.clear()
    return rows


def tabela_receita_nivel_geral(codigo, ano, mes):
    rows = db.run_query("""SELECT sum(previsto), sum(previsao_atualizada), sum(receita_arrecadada)  from 
                (SELECT ic4, (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsto, 
                    0 as previsao_atualizada, 
                    0 as receita_arrecadada
                    ,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text like  '5211%%%%' and tipo_valor = 'ending_balance'
                    group by 1,5
                    
                union all

                SELECT ic4, 0 as previsto, 
                    (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsao_atualizada,
                     0 as receita_arrecadada,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text similar to '(5211|5212)%%%%' and tipo_valor = 'ending_balance'
                    group by 1,5
                    
                union all

                SELECT ic4, 0 as previsto, 0 as previsao_atualizada, 
                    (case when natureza_valor = 'C' then sum(valor) else  sum(valor)*-1 end) as receita_arrecadada
                    ,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta in ('621200000','621300000') and tipo_valor = 'ending_balance'
                    group by 1,5) tab_receita
                """ % (codigo, ano, mes, codigo, ano, mes, codigo, ano, mes))
    st.experimental_memo.clear()
    return rows


def tabela_receita_nivel(nivel, codigo, ano, mes):
    linha = db.run_query("""select case when conta is null then 'TOTAL GERAL' else conta end,
                        previsto, previsao_atualizada , receita_arrecadada  from 
                (SELECT substring(ic4,1,%s) as conta,sum(previsto) as previsto, sum(previsao_atualizada) as previsao_atualizada, sum(receita_arrecadada) as receita_arrecadada  from 
                (SELECT ic4, (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsto, 
                    0 as previsao_atualizada, 
                    0 as receita_arrecadada
                    ,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text like  '5211%%%%' and tipo_valor = 'ending_balance'
                    group by 1,5
                    
                union all

                SELECT ic4, 0 as previsto, 
                    (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsao_atualizada,
                    0 as receita_arrecadada,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta::text similar to '(5211|5212)%%%%' and tipo_valor = 'ending_balance'
                    group by 1,5
                    
                union all

                SELECT ic4, 0 as previsto, 0 as previsao_atualizada, 
                    (case when natureza_valor = 'C' then sum(valor) else  sum(valor)*-1 end) as receita_arrecadada
                    ,natureza_valor
                    FROM public.msc
                    
                    where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                    and conta in ('621200000','621300000') and tipo_valor = 'ending_balance'
                    group by 1,5) tab_receita
                group by rollup (1)
			    order by 1) as tab""" % (nivel, codigo, ano, mes, codigo, ano, mes, codigo, ano, mes))
    st.experimental_memo.clear()
    return linha


def tabela_fonte(codigo, ano, mes):
    rows = db.run_query("""select case when conta is null then 'TOTAL GERAL' else conta end,
                        previsto, previsao_atualizada , receita_arrecadada  from 
            (SELECT ic2 as conta, sum(previsto) as previsto, sum(previsao_atualizada) as previsao_atualizada, sum(receita_arrecadada) as receita_arrecadada   from 
            (SELECT ic2, (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsto, 
                0 as previsao_atualizada, 
                0 as receita_arrecadada
                ,natureza_valor
                FROM public.msc
                
                where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                and conta::text like  '5211%%%%' and tipo_valor = 'ending_balance'
                group by 1,5
                
            union all

            SELECT ic2, 0 as previsto, 
                (case when natureza_valor = 'D' then sum(valor) else  sum(valor)*-1 end) as previsao_atualizada,
                    0 as receita_arrecadada,natureza_valor
                FROM public.msc
                
                where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                and conta::text similar to '(5211|5212)%%%%' and tipo_valor = 'ending_balance'
                group by 1,5
                
            union all

            SELECT ic2, 0 as previsto, 0 as previsao_atualizada, 
                (case when natureza_valor = 'C' then sum(valor) else  sum(valor)*-1 end) as receita_arrecadada
                ,natureza_valor
                FROM public.msc
                
                where codigo_siconfi = '%s' and ano = '%s' and mes = '%s'
                and conta in ('621200000','621300000') and tipo_valor = 'ending_balance'
                group by 1,5) tab_receita
            group by rollup (1)
			order by 1) as tab""" % (codigo, ano, mes, codigo, ano, mes, codigo, ano, mes))
    st.experimental_memo.clear()
    return rows
