from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio

cont = 10 # quantidade de elementos criados
#################################################################################
key = [] # chave a ser chamada para a arvore
char = [] # palavra aleatoria
valores_inteiros = [] # valor aleatorio
resultados=[] # soma de todas as listas

for c in range(cont): # contador que vai dar as chaves sequencialmente para cada linha
        chave = '{:001d}' .format(c)
        key.append(int(chave))

        lista = list(range(1)) # Numeros de 1 a 10.000, que ira entrar aleatoriamente 
        for i in lista:
            n = random.randint(1,10000)
            valores_inteiros.append(int(n))
        
        palavra = random.choice(palavras) # variavel que ira escolher uma palavra aleatoria do nosso modulo importado
        char.append(str(palavra))
        

for i in range(len(key)): #percorre lista con referencia no tamanho da key
   tupla=(key[i],char[i],valores_inteiros[i]) # juntando valores das listas
   resultados.append(tupla) #add
print('\n')

dict = {}
for i in range(len(resultados)):
    dict[resultados[i][0]] = resultados[i][1:]

######################################################################################
dados2 = [] # AQUI ESTA O PROBLEMA!!!!!!!!!!!!!!!!

dados2.append({
            'chave': resultados,
            
         })

with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
        for l1 in dados2:
            arquivo.write(f' {l1["chave"]} ')
            arquivo.write('\n')
            print("\n")

with open("DADOS.txt", "r") as arquivo: #ler o txt
        teste = arquivo.readlines()
        print(teste)
        
#######################################################################################

for x in dict:
    u = int(input("Digite "))
    if x == u == key:
        print(x)
    else:
        print("Não")
    
