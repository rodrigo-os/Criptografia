import platform
import os
import time
import sys
from random import sample

def redirect():
    for remaining in range(20, 0, -1):
        print('\033[?25l', end="")
        sys.stdout.write("\r")
        sys.stdout.write("Redirecionando em:{:2d}".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    print('\033[?25h', end="")

def convert(opt):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mensagem = input('Palavra|Mensagem: ')
    mensagem = mensagem.replace(" ","")
    mensagem = mensagem.lower()
    mensagem_manipulada = []
    if opt == 1:
        chave = sample(alfabeto, len(alfabeto))
        for letra in mensagem:
            if letra in alfabeto:
                index = alfabeto.index(letra)
                mensagem_manipulada.append(chave[index])
            else:
                mensagem_manipulada.append(letra)
        chave = "".join(chave)
        print(f'Chave --> {chave}')
    else:
        chave = []
        nome = input("Chave: ")
        chave[:0] = nome
        for letra in mensagem:
            if letra in chave:
                index = chave.index(letra)
                mensagem_manipulada.append(alfabeto[index])
            else:
                mensagem_manipulada.append(letra)
    mensagem_manipulada = "".join(mensagem_manipulada)
    return mensagem_manipulada
            
def clear():
    so = platform.system()
    so = str(so).lower()
    if so == 'windows':
        os.system('CLS')
    else:
        os.system('clear')

def select():
    running = True
    opt = ''
    while running:
        clear()
        print('|----------------------------------------|')
        print('| [1] - Criptografar                     |')
        print('| [2] - Descriptografar                  |')
        print('| [0] - Sair                             |')
        print('|----------------------------------------|')
        try:
            opt = int(input(':'))
        except:
            opt = ''
            print('Apenas números são aceitos!')
            time.sleep(2)
        if opt != '':
            if opt == 1:
                clear()
                mensagem = convert(opt)
                print(f'mensagem encriptografada: {mensagem}')
                print("\n")
                redirect()
            elif opt == 2:
                clear()
                mensagem = convert(opt)
                print(f'mensagem descriptografada: {mensagem}')
                print("\n")
                redirect()
            elif opt == 0:
                clear()
                print('Saindo!')
                time.sleep(2)
                running = False
            else:
                print('Opção Inválida')
                time.sleep(2)

if __name__ == "__main__":
    select()
