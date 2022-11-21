import random
from palavras import palavras

dados1 = []

def selecionar_palavras(): # função 
    palavra = random.choice(palavras) # variavel que ira escolher uma palavra aleatoria do nosso modulo importado
    return palavra.upper() # retornara a palavra escolida com letras maiusculas

def selecionar_numeros(): #colocar numero aleatorio
    lista = list(range(1,100))
    for i in lista:
        n = random.randint(1,10)
    return n

def dados_txt(valor_inteiro,char): # add no TXT
    cont = 10
    for item in range(cont):
        file = '{:01d}' .format(item) # contar
        dados1.append({
            'chave': file,
            'valor_inteiro': valor_inteiro,
            'char_1000':char 
        })
        
    with open('DADOS.txt', 'a') as arquivo:
        for l1 in dados1:
            arquivo.write(f'CHAVE: {l1["chave"]} - VALOR INTEIRO: {l1["valor_inteiro"]}- CHAR: {l1["char_1000"]}')
            arquivo.write('\n')

def iniciar():
    palavra = selecionar_palavras()
    numero = selecionar_numeros()
    dados_txt(numero,palavra)

iniciar()




  