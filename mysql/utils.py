import mysql.connector as myc

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = myc.connect(
            database='Estudos',
            host='localhost',
            user='root',
            passwd='root'
        )
        return conn
    except myc.Error as err:
        print(f'Erro na conexão ao MySQL Server: {err}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os clientes
    """
    conn = conectar()
    cursor = conn.cursor() ## Entender essa função.
    cursor.execute('SELECT * FROM Estudos.Clientes LIMIT 10')
    clientes = cursor.fetchall()

    if len(clientes) > 0:
        print('Listando Clientes...')
        print('--------------------')
        for cliente in clientes:
            print(f'IdCliente: {cliente[0]}')
            print(f'Cliente: {cliente[1]}')
            print(f'Estado: {cliente[2]}')
            print(f'Sexo: {cliente[3]}')
            print(f'Status: {cliente[4]}')
            print('--------------------')
    else:
        print('Não existem participantes.')
    desconectar(conn)


def inserir():
    """
    Função para inserir um novo cliente
    """
    conn = conectar()
    cursor = conn.cursor() 

    nome = input('Informe o nome do cliente: ')
    estado = input('Informe o estado do cliente: ')
    sexo = input('Informe o sexo do cliente: ')
    status = input('Informe o status do cartão do cliente: ')


    cursor.execute(
        f"INSERT INTO Estudos.Clientes (Cliente, Estado, Sexo, Status ) VALUES ('{nome}', {estado}, {sexo}, {status})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O cliente {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o novo cliente.')
    desconectar(conn) # Sempre fecha a conexão.


def atualizar():
    """
    Função para atualizar um cliente
    """
    
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o id do cliente: '))
    nome = input('Informe o nome do cliente: ')
    estado = input('Informe o estado do cliente: ')
    sexo = input('Informe o sexo do cliente: ')
    status = input('Informe o status do cartão do cliente: ')

    cursor.execute(
        f"UPDATE Clientes SET Cliente='{nome}', Estado='{estado}', Sexo='{sexo}', Status='{status}' WHERE IDCliente={id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O cliente {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o cliente.')
    desconectar(conn)


def deletar():
    """
    Função para deletar um cliente
    """
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Informe o id do cliente: '))

    cursor.execute(f'DELETE FROM Estudos.Clientes WHERE IDCliente={id}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Cliente excluído com sucesso.')
    else:
        print(f'Erro ao excluir o cliente com id = {id}')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Cliente Cartão de Crédito==============')
    print('Selecione uma opção: ')
    print('1 - Listar Clientes.')
    print('2 - Inserir novo cliente.')
    print('3 - Atualizar Cliente.')
    print('4 - Deletar Cliente.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
