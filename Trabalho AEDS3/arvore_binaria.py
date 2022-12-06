from fila import Fila # importação de fila
from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio
import time
import timeit
import json

ROOT= "raiz"
class No: #classe que vai indicar os dados e direita esquesrda
    def __init__(self,dado):
        self.dado = dado
        self.esquerda = None #filho a esquerda
        self.direita = None #filho a direita

    def __str__(self): #converter um No em str
        return str(self.dado)  #retorna o dado em forma de str

class ArvoreBinaria: #arvore 
    def __init__(self,dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado) #no vai ser igual ao dado inserido en No
            self.raiz = no # a raiz da arvore vai ser igual ao dado
        else:
            self.raiz = None
    #percurso simetrico
    def percurso_simetrico(self, no=None): 
        if no is None:
            no = self.raiz
        if no.esquerda:
            print('(', end=" ") # colocar o ( no inicio , end não pular linha
            self.percurso_simetrico(no.esquerda)
        print(no, end=" ") # colocar para a lateral 
        if no.direita:
            self.percurso_simetrico(no.direita)
            print(')', end=" ") # colocar o ) no final
    #percurso pos ordem
    #ira percorrer a arvore da esquerda para direira de seu maior nivel 
    #depois ira para a direita em seu maior nivel 
    #depois para a raiz
    def percurso_pos_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.percurso_pos_ordem(no.esquerda)
        if no.direita:
            self.percurso_pos_ordem(no.direita)
        print(no)
    
    def altura(self, no=None): # ira verificar a altura da arvore
        if no is None:
            no = self.raiz
        Aesquerda = 0
        Adireita = 0

        if no.esquerda:
            Aesquerda = self.altura(no.esquerda)
        if no.direita:
            Adireita = self.altura(no.direita)
        if Adireita > Aesquerda: # contador de altura da arvore
            return Adireita + 1
        else:
            return Aesquerda + 1
    
    def in_ordem_simetrica(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.in_ordem_simetrica(no.esquerda)
        print(no, end=' ')
        if no.direita:
            self.in_ordem_simetrica(no.direita)
    
    def percurso_nivel(self, no=ROOT):
        if no == ROOT:
            no = self.raiz

        fila = Fila()
        fila.empurre(no)
        while len(fila):
            no = fila.pop()
            if no.esquerda:
                fila.empurre(no.esquerda)
            if no.direita:
                fila.empurre(no.direita)
            print(no, end=" ")
           

# herdar a qualidades da Arvore Binaria
class ArvoreBinariaBusca(ArvoreBinaria):
    
    def insert(self, valor): # inserindo valores
        pai = None
        x = self.raiz
        while(x):
            pai = x
            if valor < x.dado:
                x = x.esquerda
            else:
                x = x.direita
        if pai is None:
            self.raiz = No(valor)
        elif valor < pai.dado:
            pai.esquerda = No(valor)
        else:
            pai.direita = No(valor)
    
    def procurar(self, valor): # função que ira procurar os valores selecionados
        return self._procurar(valor, self.raiz)

    def _procurar(self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreBinariaBusca(no)
        if valor < no.dado:
            return self._procurar(valor, no.esquerda)
        return self._procurar(valor, no.direita)
        

####################################################################################################
#INICIO 
cont = int(input("Digite o Valor de Vezes a ser Processador os Dados:  ")) # quantidade de elementos criados
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
elemento = random.shuffle(resultados) # bagunça na lista

#transforma lista em Biblioteca
dict = {}
for i in range(len(resultados)):
    dict[resultados[i][0]] = resultados[i][1:]

# JSON para escrever os dados do arquivo no TXT
json.dump(resultados, open('DADOS_Arvore_BINARIA.txt', 'w'))
    
def example_arvore():
#ler o arquivo txt criado usando o json
    teste = json.load(open("DADOS_Arvore_BINARIA.txt", "r"))
    inlist = { x[0]: (x[1], x[2])  for x in teste }
    arvore = ArvoreBinariaBusca()
    for v in inlist:
        arvore.insert(v)
    return arvore

#######################################################################################
print('\n---Ordem Simetrica---') # lista em ordem
abb = example_arvore()
abb.in_ordem_simetrica()
print('\n')

u = int(input("Digite o Valor a ser BUSCADO:: "))
items = [u] # a busca na nossa arvore
ini = time.time()
for elementos in items:
    r = abb.procurar(elementos) # metodo de busca na arvore
    if r is None:
        print(elementos, "Não encontrado")
    else:
        print(r.raiz.dado, 'encontrado')
        print(dict.get(u))

    #Contador de Doração da procura na arvore com valores ordenados    
    time.sleep(1)
inicio = timeit.default_timer()
fim = timeit.default_timer()
print ('Duracao Da Procura Na Arvore Binaria Ordem Simetrica: %5f' % (fim - inicio))
fim = time.time()
print ("TEMPO-Ordem Simetrica: ", (fim-ini) ,"Segundos")
    
#######################################################################################
print('\n----Ordem Aleatório---') # Orden que esta sendo inserida na arvore 
abb.percurso_nivel()
print("\n")

u = int(input("Digite o Valor a ser BUSCADO:: "))
items = [u] # a busca na nossa arvore
inii = time.time()
for elementos in items:
    r = abb.procurar(elementos) # metodo de busca na arvore
    if r is None:
        print(elementos, "Não encontrado")
        
    else:
        print(r.raiz.dado, 'Encontrado')
        print(dict.get(u))

    #Contador de Doração da procura na arvore com valores aleatorios    
    time.sleep(1) #
inicio = timeit.default_timer()
fim = timeit.default_timer()
print ('Duracao Da Procura Na Arvore Binaria Ordem Aleatoria: %f' % (fim - inicio))
fimm = time.time()
print ("TEMPO-Ordem Aleatoria: ", (fimm-inii) ,"Segundos")
#######################################################################################

