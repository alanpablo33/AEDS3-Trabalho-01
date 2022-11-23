import random
from palavras import palavras

dados1 = []
cont = 10# Local a Testar Valores

def dados_txt(): # add no TXT
    
    for c in range(cont): # contador que vai dar as chaves sequencialmente para cada linha
        chave = '{:01d}' .format(c) 

        lista = list(range(1)) # Numeros de 1 a 10.000, que ira entrar aleatoriamente 
        for i in lista:
            n = random.randint(1,10000)
        
        palavra = random.choice(palavras) # variavel que ira escolher uma palavra aleatoria do nosso modulo importado
        
        #lista a ser preenchida com CHAVE,INTEIRO e CHAR
        dados1.append({
            'chave': chave,
            'valor_inteiro': n,
            'char_1000':palavra 
         })
        
    with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
        for l1 in dados1:
            arquivo.write(f' {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]}- CHAR: {l1["char_1000"]}')
            arquivo.write('\n')
    
dados_txt()









