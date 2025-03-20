'''
    Crei uma função chamado "gerar_objeto_personalizado" que irá receber 3 parâmetros, cor, altura e formato.
    A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
    Porém ela deve seguir as seguintes regras:

    1. O primeiro nargumento deve ser posicional 
    2. Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados.
'''

def gerar_objeto_personalizado(cor,*, altura, formato):

    print(cor, altura, formato)

gerar_objeto_personalizado('Azul', altura= 1.78, formato= 'quadrado')    