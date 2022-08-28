import mysql.connector

# conxeão com banco de dados sistema_login
try:
    global conexão, cursor
    conexão = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_login'
    )
    cursor = conexão.cursor()
except Exception as erro:
    print(f'Falha a conexão com banco de dados. ERRO [{erro.__class__}] ')
else:
    print('Conexão com banco de dados feita com sucesso')


# Sistema de login
def cadastroUsuario(cadastro_nome, cadastro_senha):

    comando_inserir = f'''INSERT INTO usuarios VALUES
    (DEFAULT,'{cadastro_nome}','{cadastro_senha}');
    '''
    cursor.execute(comando_inserir)
    conexão.commit()
    print('Usuário cadastrado com sucesso!')


def exibirCadastrados():
    cursor.execute('SELECT * FROM usuarios;')
    consultaBanco = cursor.fetchall()
    if consultaBanco == []:
        print('Banco de dados vázio!')
    for linha in consultaBanco:
        print(linha)


def logarNoSistema(login_nome, login_senha):

    comando_coletar = f'''SELECT username,senha FROM usuarios
        WHERE username = '{login_nome}';
        '''
    cursor.execute(comando_coletar)
    dados = cursor.fetchall()

    if login_nome == dados[0][0]:
        if login_senha == dados[0][1]:
            print(f'{login_nome} Logado com sucessor!')
        else:
            print('Senha incorreta!')
    else:
        print('Nome incorreto!')


while True:
    print('Sistema')
    print('''
    [0] logar
    [1] Cadastra usuario
    [2] Sair do sistema
    [3] Exibir contas cadastradas\n''')
    opç = int(input('Digite um numero inteiro > '))

    if opç == 0:
        logarNoSistema(str(input('nome > ')),
                       str(input('senha > ')))
    elif opç == 1:
        cadastroUsuario(str(input('Digite nome > ')),
                        str(input('Digite senha > ')))
    elif opç == 3:
        exibirCadastrados()
    elif opç == 2:
        print('Saindo...')
        break
    else:
        print('Numero não encontrado, Tente novamente!')
        continue
