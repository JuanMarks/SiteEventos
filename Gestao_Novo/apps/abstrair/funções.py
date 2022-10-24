def diretorio_excel(arquivo,post_files):
    for arq in arquivo:
        arq2 = f"{arq.arquivo}"
        arq2_split = arq2.split('/')
        if arq2_split[5] == f"{post_files}":
            return f"{arq2}"

def pegar_dados(arq_excel):
    """
    Pegar Dados é uma função que tem como intuito se utilizar
    dos dados fornecidos pela biblioteca pyexcel, que ao ler 
    o arquivo excel retorna para o usuário uma lista bidimensional

    Essa função pode ser adequada de acordo com a necessidade do
    usuário, mas no momento serve para 'Pegar os NOMES' e 'EMAILS'
    vindo do arquivo excel

    para retornar os valores, basta usar a variável que foi declarada
    e o identificador

    Por Exemplo: valores = pegar_dados(arq_excel)
                 print(valores['nomes'])
                 print(valores['emails'])
    """
    indice_nome = 0
    indice_email = 0
    
    nomes = []
    emails = []
    for linha in arq_excel:
        if "nome" in linha:
            indice_nome += linha.index('nome')
        if "email" in linha:
            indice_email += linha.index('email')
    n = 0
    for linha in arq_excel:
        if n == 0:
            n += 1
        else:
            nomes.append(linha[indice_nome])
            emails.append(linha[indice_email])
            n += 1
    
    valores = {
        'nomes': nomes,
        'emails': emails
    }
    return valores

def comparar_grupos(grupo):
    if grupo == "USR":
        gp = "Usuario"
    elif grupo == "ADM":
        gp = "Administrador"
    elif grupo == "MANTENEDOR":
        gp = "Mantenedor"
    elif grupo == "ALL":
        gp = "Todos"
    else:
        gp = "Escolha uma opção"
    return gp