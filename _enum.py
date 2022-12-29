import services.database as db


def enum_telas():
    telas = ["Cidade", "Importar Arquivo", "Receita", "Despesa"]
    return telas


def enum_funcionalidadeas():
    funcionalidades = ["Cadastrar", "Consultar", "Excluir", "Alterar"]
    return funcionalidades


def enum_cidade():
    cidade_lista = []
    rows = db.run_query("SELECT nome from cidade;")
    for row in rows:
        cidade_lista.append(''.join(row))
    return cidade_lista
