import PySimpleGUI as sg

def realizarLogin(usuario, senha):
    with open ('logins.txt') as arquivoUsuario:
        logins = arquivoUsuario.readlines()

    for i in range (len(logins)):
        if(usuario+senha == logins[i]):
            return True
        
    return False

def cadastrarLogin (usuarioCadastro, senhaCadastro):
    with open('logins.txt', 'a') as arquivoUsuario:
        arquivoUsuario.write('\n' + usuarioCadastro+senhaCadastro)


designer = [
    [sg.Text ('Usuário')], 
    [sg.Input (key = 'usuario')],
    [sg.Text ('Senha')],
    [sg.Input (key = 'senha', password_char='*')],
    [sg.Button ('Login')],
    [sg.Text ('', key= 'mensagem')],
    [sg.Button ('Cadastrar')],
]

window = sg.Window ('Login', layout = designer)

cadastrar = [
    [sg.Text ('Usuário')], 
    [sg.Input (key = 'usuario')],
    [sg.Text ('Senha')],
    [sg.Input (key = 'senha',password_char='*')],
    [sg.Button ('Salvar')],
    [sg.Text ('', key= 'mensagem')],
]

windowcadastra = sg.Window ('Cadastrar', layout = cadastrar)


while True: 
    event, values = window.read ()
    if event == sg.WIN_CLOSED:
        break 
    
    match(event):
        case 'Login':
            usuario = values['usuario']
            senha = values['senha']
            logou= realizarLogin(usuario, senha)
            if (logou):
                window ['mensagem'].update ('Login realizado com sucesso')
            else:
                window ['mensagem'].update ('Login ou senha inválidos')

        case 'Cadastrar':
            while True: 
                event, values = windowcadastra.read ()
                if event == sg.WIN_CLOSED:
                    break 
                
                usuarioCadastro = values['usuario']
                senhaCadastro= values['senha']
                cadastrar= cadastrarLogin(usuarioCadastro, senhaCadastro)
                windowcadastra ['mensagem'].update ('Cadastro realizado com sucesso')
                windowcadastra.close ()
            