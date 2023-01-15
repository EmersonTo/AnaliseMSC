import services.database as db


def retorna_codigo_cidade(cidade):
    row = db.run_query("""SELECT codigo_siconfi FROM public.cidade where nome = '%s'"""
                       % (cidade))
    return row
