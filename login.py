import mysql.connector 

#conxeão com banco de dados sistema_login
try:
    conexão = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'sistema_login'
    )
except Exception as erro:
    print(f'Falha a conexão com banco de dados. ERRO [{erro.__class__}] ')
else:
    print('Conexão com banco de dados feita com sucesso')

cursor = conexão.cursor()




#Sistema de login
def cadastro_usuario():

    print('Tela de cadastro')
    cadastro_nome = str(input('Digite um username:')) 
    cadastro_senha = str(input('Digite uma senha'))

    def inserir_dados():
        comando_inserir = f'''INSERT INTO usuarios VALUES
        (DEFAULT,'{cadastro_nome}','{cadastro_senha}');
        '''
        cursor.execute(comando_inserir)
        conexão.commit()
        print('Usuário cadastrado com sucesso!')
        inserir_dados()
def exibir():
    cursor.execute('SELECT * FROM usuarios;')
    res = cursor.fetchall()
    for linha in res:
        print(linha)

def login(): 
    #logar 
    print('Faça seu login')
    login_nome = str(input('Nome:'))
    login_senha = str(input('Senha:'))

    def verificação():
            comando_coletar = f'''SELECT username,senha FROM usuarios
            WHERE username = '{login_nome}';
            '''
            cursor.execute(comando_coletar)
            dados = cursor.fetchall()

            if login_nome == dados[0][0]:
                print('nome correto!')
                if login_senha == dados[0][1]:
                    print('Senha correta!')
                    print(f'{login_nome} Logado com sucessor!')
            else:
                print('Nome ou senha incorreto!')
    verificação()


while True:
    print('Sistema')
    print('''
    [0] logar
    [1] Cadastra usuario
    [2] Sair 
    [3] Exibir tudo''')
    opç = int(input('Digite um numero inteiro:'))

    if opç == 0:
        login()
    elif opç == 1:
        cadastro_usuario()
    elif opç == 3:
        exibir()
    elif opç == 2:
        print('Parando...')
        break
    else:
        print('Deu ruim')