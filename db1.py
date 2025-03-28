import PySimpleGUI as sg
import datetime


def registrar_log(mensagem):
    with open("audit_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {mensagem}\n")


def realizarLogin(usuario, senha):
    try:
        with open('logins.txt', 'r') as arquivoUsuario:
            logins = arquivoUsuario.readlines()

        for linha in logins:
            if f"{usuario}:{senha}" == linha.strip():
                registrar_log(f"Login bem-sucedido para {usuario}")
                return True
    except FileNotFoundError:
        registrar_log(f"Tentativa de login falhou para {usuario} - Arquivo não encontrado")
        return False

    registrar_log(f"Tentativa de login falhou para {usuario} - Credenciais incorretas")
    return False


def cadastrarLogin(usuarioCadastro, senhaCadastro):
    with open('logins.txt', 'a') as arquivoUsuario:
        arquivoUsuario.write(f'{usuarioCadastro}:{senhaCadastro}\n')
    registrar_log(f"Novo usuário cadastrado: {usuarioCadastro}")

layout_login = [
    [sg.Text('Usuário')], 
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('Login'), sg.Button('Cadastrar')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout=layout_login)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Login':
        usuario = values['usuario']
        senha = values['senha']
        if realizarLogin(usuario, senha):
            window['mensagem'].update('Login realizado com sucesso', text_color='green')
        else:
            window['mensagem'].update('Login ou senha inválidos', text_color='red')

    elif event == 'Cadastrar':
        layout_cadastro = [
            [sg.Text('Usuário')],
            [sg.Input(key='usuario')],
            [sg.Text('Senha')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Button('Salvar')],
            [sg.Text('', key='mensagem')],
        ]
        window_cadastro = sg.Window('Cadastrar', layout=layout_cadastro)

        while True:
            event_cadastro, values_cadastro = window_cadastro.read()
            if event_cadastro == sg.WIN_CLOSED:
                break

            if event_cadastro == 'Salvar':
                usuarioCadastro = values_cadastro['usuario']
                senhaCadastro = values_cadastro['senha']
                
                if usuarioCadastro and senhaCadastro:
                    cadastrarLogin(usuarioCadastro, senhaCadastro)
                    window_cadastro['mensagem'].update('Cadastro realizado com sucesso', text_color='green')
                else:
                    window_cadastro['mensagem'].update('Preencha todos os campos!', text_color='red')

        window_cadastro.close()

window.close()
