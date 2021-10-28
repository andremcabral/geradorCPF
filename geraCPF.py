from random import randint
import PySimpleGUI as sg

def identificaUF(i):
    if (i == 1):
        uf = 'Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins'
    elif (i == 2):
        uf = 'Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima'
    elif (i == 3):
        uf = 'Ceará, Maranhão ou Piauí'
    elif (i == 4):
        uf = 'Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas'
    elif (i == 5):
        uf = 'Bahia ou Sergipe'
    elif (i == 6):
        uf = 'Minas Gerais'
    elif (i == 7):
        uf = 'Rio de Janeiro ou Espírito Santo'
    elif (i == 8):
        uf = 'São Paulo'
    elif (i == 9):
        uf = 'Paraná ou Santa Catarina'
    elif (i == 0):
        uf = 'Rio Grande do Sul'
    return uf

layout=[
    [sg.Button('Gerar um CPF aleatório e válido', size=(30,0), key='gerarNovo')],
    [sg.Text('CPF (Digite apenas números)', size=(30, 0))],
    [sg.InputText(size=(15, 0), key='cpf', do_not_clear=False)],
    [sg.Button('Identificar dígitos verificadores', size=(30, 0), key='digitos', disabled=False)],
    # [sg.Output(size=(32,6))],
    [sg.Button('Sair', size=(30, 2), key='sair')]
]
janela = sg.Window('Gerador de CPF').layout(layout)

def calculaCPF():
    soma = (a * 10) + (b * 9) + (c * 8) + (d * 7) + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
    if ((soma % 11) <= 1):
        x = 0
    else:
        x = 11 - (soma % 11)
    soma = (a * 11) + (b * 10) + (c * 9) + (d * 8) + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (
            x * 2)
    if ((soma % 11) <= 1):
        z = 0
    else:
        z = 11 - (soma % 11)
    return f"{a}{b}{c}.{d}{e}{f}.{g}{h}{i}-{x}{z}"

while True:
    Button, values = janela.Read()
    if (Button == 'sair' or Button == sg.WINDOW_CLOSED):
        break
    else:
        if (Button == 'gerarNovo'):
            a = randint(0, 9)
            b = randint(0, 9)
            c = randint(0, 9)
            d = randint(0, 9)
            e = randint(0, 9)
            f = randint(0, 9)
            g = randint(0, 9)
            h = randint(0, 9)
            i = randint(0, 9)
            respCpf = calculaCPF()
            uf = identificaUF(i)
            print(f"{respCpf} - Foi gerado na UF: {uf}")
        if (Button == 'digitos'):
            if(values['cpf']=='' or (len(values['cpf'])>9) or (len(values['cpf'])<9)):
                print('Informe o 9 números sem pontuação')
                cpf=int(999999999)
            else:
                cpf = values['cpf']
                cpf=int(cpf)
                a = cpf // 100000000 % 10
                b = cpf // 10000000 % 10
                c = cpf // 1000000 % 10
                d = cpf // 100000 % 10
                e = cpf // 10000 % 10
                f = cpf // 1000 % 10
                g = cpf // 100 % 10
                h = cpf // 10 % 10
                i = cpf // 1 % 10
                respCpf = calculaCPF()
                uf=identificaUF(i)
                print(f"{respCpf} - Foi gerado na UF: {uf}")