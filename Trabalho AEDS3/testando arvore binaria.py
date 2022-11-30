#PERCURSO em NÍVEL em ÁRVORE BINÁRIA 
import random
from arvore_binaria import ArvoreBinariaBusca
from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio


dados1= [] #Global
cont = 21 # quantidade de elementos criados

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
#x = int(input("Digite: "))
#print(resultados[x])

#############################################################################################################

dados1.append({
            'chave': key,
            'valor_inteiro': valores_inteiros,
            'char_1000':char 
         })

with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
        for l1 in dados1:
            arquivo.write(f' CHAVE: {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]} CHAR: {l1["char_1000"]}')
            arquivo.write('\n')

with open('DADOS2.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
        for l1 in dados1:
            arquivo.write(f' CHAVE: {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]} CHAR: {l1["char_1000"]}')
            arquivo.write('\n')


with open("DADOS2.txt", "r") as arquivo: #ler o txt
        teste = arquivo.readlines()
        w= random.sample(teste,len(teste)) #valores do arquivo txt DADOS2 aleatorios
        print('\n')




#random.seed(77)

#def random_arvore(size=42):
#    valor = random.sample(range(1, 1000), 42)
#    arvore = ArvoreBinariaBusca()
#    for v in valor:
#        arvore.insert(v)
#    return arvore

def example_arvore():
        
    valor = key
    arvore = ArvoreBinariaBusca()
    for v in valor:
        arvore.insert(v)
    return arvore


print('\n---Ordem Simetrica---') # lista em ordem
abb = example_arvore()
abb.in_ordem_simetrica()
print('\n')

print('\n----Ordem Aleatório---') # Orden que esta sendo inserida na arvore 
abb.percurso_nivel()
print('\n')

print("\n")




items = int(input("Digite: ")) # a busca na nossa arvore

for elementos in items:
    r = abb.procurar(elementos)
    if r is None:
        print(elementos, "Não encontrado")
    else:
        print(r.raiz.dado, 'encontrado')
        print(key[items])




