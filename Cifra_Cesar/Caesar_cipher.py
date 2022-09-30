import platform
import os
import time
import sys

def redirect():
    for remaining in range(10, 0, -1):
        print('\033[?25l', end="")
        sys.stdout.write("\r")
        sys.stdout.write("Redirecionando em:{:2d}".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    print('\033[?25h', end="")

def converter(opt):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mensagem = input('Palavra|Mensagem: ')
    mensagem = mensagem.replace(" ","")
    mensagem = mensagem.lower()
    chave = int(input('Chave: '))
    mensagem_manipulada = ''
                
    for letra in mensagem:
        index_mensagem = alfabeto.find(letra)
        if index_mensagem == -1:
            mensagem_manipulada += letra
        else:
            if opt == 1: 
                index_mensagem_manipulada = index_mensagem + chave
            else:
                index_mensagem_manipulada = index_mensagem - chave
            index_mensagem_manipulada = index_mensagem_manipulada % len(alfabeto)
            mensagem_manipulada += alfabeto[index_mensagem_manipulada]
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
                mensagem = converter(opt)
                print(f'mensagem encriptografada: {mensagem}')
                print("\n")
                redirect()
            elif opt == 2:
                clear()
                mensagem = converter(opt)
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
