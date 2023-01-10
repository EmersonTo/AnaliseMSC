import services.database as db


def enum_telas():
    telas = ["Cidade", "Importar Arquivo", "Receita", "Despesa"]
    return telas


def enum_funcionalidadeas():
    funcionalidades = ["Cadastrar", "Consultar", "Excluir", "Alterar"]
    return funcionalidades


def enum_mes():
    enum_mes = ["01", "02", "03", "04", "05",
                "06", "07", "08", "09", "10", "11", "12"]
    return enum_mes

def enum_anos():
    enum_ano = ["2020","2021","2022"]
    return enum_ano


def enum_receitas():
    tipos = ["Resumo", "Evolução"]
    return tipos


def enum_cidade():
    cidade_lista = []
    rows = db.run_query("SELECT nome from cidade;")
    for row in rows:
        cidade_lista.append(''.join(row))
    return cidade_lista
