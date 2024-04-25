import oracledb

def db_usuario():
    try:
        # Estabelecer conexão com o banco de dados de produtos
        conexao_usuario = oracledb.connect(user="BD150224532", password="Zthrh10", host="172.16.12.14", port=1521)
        print("BANCO DE DADOS CONECTADO COM SUCESSO!")
        return conexao_usuario
    except Exception as e:
        print(f"ERRO AO CONECTAR COM O BANCO DE DADOS DOS USUÁRIOS: {str(e)}")
        return None

def db_produtos():
    try:
        conexao_produtos = oracledb.connect(user="BD150224532", password="Zthrh10", host="172.16.12.14", port=1521)
        print("BANCO DE DADOS CONECTADO COM SUCESSO!")
        return conexao_produtos
    except Exception as e:
        print(f"ERRO AO CONECTAR COM O BANCO DE DADOS DOS PRODUTOS: {str(e)}")
        return None

def fechar_conexao(conexao):
    try:
        conexao.close()
        print("CONEXÕES FECHADAS COM SUCESSO.")
    except Exception as e:
        print(f"ERRO AO FINALIZAR A CONEXÃO: {str(e)}")
