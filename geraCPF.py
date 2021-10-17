from random import randint
## INFORMAÇÃO DE ESTADO ONDE FOI EMITIDO O CPF, PELO ÚLTIMO DÍGITO ANTES DO '-'
# 1 - Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins;
# 2 - Pará, Amazonas, Acre, Amapá, Rondônia e Roraima;
# 3 - Ceará, Maranhão e Piauí;
# 4 - Pernambuco, Rio Grande do Norte, Paraíba e Alagoas;
# 5 - Bahia e Sergipe;
# 6 - Minas Gerais;
# 7 - Rio de Janeiro e Espírito Santo;
# 8 - São Paulo;
# 9 - Paraná e Santa Catarina;
# 0 - Rio Grande do Sul.

def identificaEstado(i):
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

def gerador():
    escolher = 9
    while (escolher != 0):
        escolher =  int(input('Escolha a opção desejada:\n1) Número aleatório\n2) Descobrir dígitos verificadores\n0) Sair\n'))
        if (escolher==1):
            a = randint(0, 9)
            b = randint(0, 9)
            c = randint(0, 9)
            d = randint(0, 9)
            e = randint(0, 9)
            f = randint(0, 9)
            g = randint(0, 9)
            h = randint(0, 9)
            i = randint(0, 9)
        elif( escolher==2):
            numero = int(input(f'Numero sem pontuação nem dígitos verificadores:\n'))
            i = numero // 1 % 10
            h = numero // 10 % 10
            g = numero // 100 % 10
            f = numero // 1000 % 10
            e = numero // 10000 % 10
            d = numero // 100000 % 10
            c = numero // 1000000 % 10
            b = numero // 10000000 % 10
            a = numero // 100000000 % 10
        elif (escolher == 0):
            break
        else:
            print('valor incorreto')

        soma = (a*10) + (b*9) + (c*8) + (d*7) + (e*6) + (f*5) + (g*4) + (h*3) + (i*2)
        if((soma%11)<=1):
            x=0
        else:
            x=11-(soma%11)
        soma = (a*11) + (b*10) + (c*9) + (d*8) + (e*7) + (f*6) + (g*5) + (h*4) + (i*3) + (x*2)
        if((soma%11)<=1):
            z=0
        else:
            z=11-(soma%11)

        uf=identificaEstado(i)

        print(f"{a}{b}{c}.{d}{e}{f}.{g}{h}{i}-{x}{z}")
        print(f'CPF gerado na UF: {uf}')

if __name__ == '__main__':
    gerador()