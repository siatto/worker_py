# Conector recomendado na documentação oficial.
import pyodbc


def conectar_mssql_docker(usuario, senha):
    con = pyodbc.connect(
        # Driver que será utilizado na conexão
        'DRIVER={SQL Server};'
        # IP ou nome do servidor.
        'SERVER=den1.mssql8.gear.host;'
        # Porta
        'PORT=1433;'
        # Banco que será utilizado.
        'DATABASE=mssqlerp;'
        # Nome de usuário.
        f'UID={usuario};'
        # Senha (novasenha@123).
        f'PWD={senha}')

    # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
    cur = con.cursor()
    return cur


if __name__ == "__main__":
    usuario = str(input('Usuario: '))
    print(usuario)
    senha = str(input('Senha: '))
    print(senha)

    cursor = conectar_mssql_docker(usuario=usuario, senha=senha)
    #cursor.execute("SELECT * FROM [mssqlerp].[dbo].[PRODUTO]");
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()

    print(row[0])