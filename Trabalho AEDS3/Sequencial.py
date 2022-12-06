from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio
import time
import timeit
import json

# quantidade de elementos criados
cont = int(input("Digite o Valor de Vezes a ser Processador os Dados:  ")) 
print("\n")
key = [] # chave a ser chamada para a arvore
char = [] # palavra aleatoria
valores_inteiros = [] # valor aleatorio
resultados=[] # soma de todas as listas
resultados2=[]

# contador que vai dar as chaves sequencialmente para cada linha
for c in range(cont): 
        chave = '{:001d}' .format(c)
        key.append(int(chave))

        lista = list(range(1)) # Numeros de 1 a 10.000, que ira entrar aleatoriamente 
        for i in lista:
            n = random.randint(1,10000)
            valores_inteiros.append(int(n))
        
        palavra = random.choice(palavras) # variavel que ira escolher uma palavra aleatoria do nosso modulo importado
        char.append(str(palavra))

#recebe valores e joga dentro de uma lista com tupla  
#percorre lista con referencia no tamanho da key
for i in range(len(key)): 
   # juntando valores das listas
   tupla=(key[i],char[i],valores_inteiros[i]) 
   resultados.append(tupla) #add
   resultados2.append(tupla) #add

#transforma lista em Biblioteca
dict = {}
for i in range(len(resultados)):
    dict[resultados[i][0]] = resultados[i][1:]

#transforma lista em Biblioteca
dict2 = {}
for i in range(len(resultados2)):
    dict[resultados2[i][0]] = resultados2[i][1:]
element = random.shuffle(resultados2) # bagunça na lista

# JSON para escrever os dados do arquivo no TXT
json.dump(resultados, open('DADOS_SEQUENCIAL.txt', 'w'))
    
#ler o arquivo txt criado usando o json
teste = json.load(open("DADOS_SEQUENCIAL.txt", "r"))
inlist = { x[0]: (x[1], x[2])  for x in teste }
print("\n")

# JSON para escrever os dados do arquivo no TXT
json.dump(resultados2, open('DADOS_SEQUENCIAL_Aleatorio.txt', 'w'))
    
#ler o arquivo txt criado usando o json
teste2 = json.load(open("DADOS_SEQUENCIAL_Aleatorio.txt", "r"))
inlist2 = { x[0]: (x[1], x[2])  for x in teste2}
print("\n")

u = int(input("Digite o Valor a ser BUSCADO na Lista Simetrica: "))
ini = time.time()
for elemento in inlist:
    if elemento == u:
        print(">>>>> Ordem Simetrica <<<<<")
        print("Chave de valor:",u, "Encontrado")
        print(dict.get(u))

        time.sleep(1) 
        inicio = timeit.default_timer()
        fim = timeit.default_timer()
        print ('Duracao Da Procura Sequencial Ordem Simetrica: %f' % (fim - inicio))
        break
fim = time.time()
print ("TEMPO-Ordem Simetrica: ", (fim-ini) ,"Segundos")

print("\n")

t = int(input("Digite o Valor a ser BUSCADO Na Lista Aleatoria: "))
inii = time.time()
for elemento2 in inlist2:
    if elemento2 == t:
        print(">>>>> Ordem Aleatoria <<<<<")
        print("Chave de valor:",t, "Encontrado")
        print(dict.get(t))

        time.sleep(1) 
        inicio = timeit.default_timer()
        fim = timeit.default_timer()
        print ('Duracao Da Procura Sequencial Ordem Aleatoria: %f' % (fim - inicio))
        break
fimm = time.time()
print ("TEMPO-Ordem Aleatoria: ",(fimm-inii),"Segundos")
        
