import sqlite3


def add():
    bd = sqlite3.connect('clientes_rt.db')
    cursor = bd.cursor()

    nome = input('Nome: ')
    apelido = input('Apelido: ')
    entradas = float(input('Entradas: '))
    saldo = int(input('Saldo: '))
    moedas_rt = int(input('Moedas RT: '))
    creditos = int(input('Creditos: '))
    create = f'INSERT INTO clientes (Nome, Apelido, Entradas, Saldo, "Moedas RT", Creditos) VALUES ("{nome}","{apelido}", "{entradas}", "{saldo}", "{moedas_rt}", "{creditos}")'

    cursor.execute(create)
    bd.commit()

    cursor.close()
    bd.close()


def consultar():
    clientes_rt = sqlite3.connect('clientes_rt.db')
    cursor = clientes_rt.cursor()

    nome = input('Nome: ')
    read = "SELECT * FROM clientes WHERE Nome LIKE '%" + nome + "%' "

    cursor.execute(read)
    result = cursor.fetchall()
    print(result)

    cursor.close()
    clientes_rt.close()


def update():
    clientes_rt = sqlite3.connect('clientes_rt.db')
    cursor = clientes_rt.cursor()

    nome = input('Nome: ')
    apelido = input('Apelido: ')
    entradas = float(input('Entradas: '))
    saldo = int(input('Saldo: '))
    moedas_rt = int(input('Moedas RT: '))
    creditos = int(input('Creditos: '))
    update = f'UPDATE clientes SET Entradas = "{entradas}", Saldo = "{saldo}", "Moedas RT" = "{moedas_rt}", Creditos = "{creditos}" WHERE Nome = "{nome}" AND Apelido = "{apelido}"'

    cursor.execute(update)
    clientes_rt.commit()

    cursor.close()
    clientes_rt.close()


def remove():
    bd = sqlite3.connect('clientes_rt.db')
    cursor = bd.cursor()

    nome = input('Nome: ')
    apelido = input('Apelido: ')
    delete = f'DELETE FROM clientes WHERE Nome = "{nome}" AND Apelido = "{apelido}"'

    cursor.execute(delete)
    bd.commit()

    cursor.close()
    bd.close()


def menu():
    print("")
    print("Base de Dados RT")
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Alterar")
    print("4 - Excluir")
    print("")
    opcao = int(input("Escolha a opcao desejada: "))
    print("")

    if opcao == 0:
        print("")

    elif opcao == 1:
        add()

    elif opcao == 2:
        consultar()

    elif opcao == 3:
        update()

    elif opcao == 4:
        remove()

    else:
        print("Escolha a opcao 0, 1, 2, 3 ou 4.")

menu()
