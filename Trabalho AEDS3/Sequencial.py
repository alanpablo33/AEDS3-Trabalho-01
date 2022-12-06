from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio
import time
import timeit
import json

cont = int(input("Digite o Valor de Vezes a ser Processador os Dados:  ")) # quantidade de elementos criados
print("\n")
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

      #recebe valores e joga dentro de uma lista com tupla  
for i in range(len(key)): #percorre lista con referencia no tamanho da key
   tupla=(key[i],char[i],valores_inteiros[i]) # juntando valores das listas
   resultados.append(tupla) #add
aleatorio = random.shuffle(resultados) # bagunça na lista
print(aleatorio)


#transforma lista em Biblioteca
dict = {}
for i in range(len(resultados)):
    dict[resultados[i][0]] = resultados[i][1:]

#######################################
# JSON para escrever os dados do arquivo no TXT
json.dump(resultados, open('DADOS_SEQUENCIAL.txt', 'w'))
    
#ler o arquivo txt criado usando o json
teste = json.load(open("DADOS_SEQUENCIAL.txt", "r"))
inlist = { x[0]: (x[1], x[2])  for x in teste }
u = int(input("Digite o Valor a ser BUSCADO: "))
print("\n")

for elemento in inlist:
    if elemento == u:
        print(">>>>> Ordem Simetrica <<<<<")
        print("Chave de valor: ",u, "Encontrado")
        print(dict.get(u))

        time.sleep(1) 
        inicio = timeit.default_timer()
        fim = timeit.default_timer()
        print ('Duracao Da Procura Sequencial Ordem Aleatoria: %f' % (fim - inicio))
        break
else:
    print("Não Encontrado!")
        
