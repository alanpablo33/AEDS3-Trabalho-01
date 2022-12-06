from fila import Fila # importação de fila
from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio
import time
import timeit



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
dados1 = []
dados2 = []
cont = 25# Local a Testar Valores


    
for c in range(cont): # contador que vai dar as chaves sequencialmente para cada linha
        chave = '{:001d}' .format(c)
        chave1 = '{:001d}' .format(c) 
    

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
    
with open('DADOS2.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
        for l1 in dados1:
            arquivo.write(f' {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]}- CHAR: {l1["char_1000"]}')
            arquivo.write('\n')

with open("DADOS2.txt", "r") as arquivo: #converte para lista
        teste = arquivo.readlines()
        print(teste)
        x= random.sample(teste,len(teste)) #valores do arquivo txt DADOS2 aleatorios
        print("\n\n\n")
        print(x)
        print('\n')
        
with open("DADO3.txt", "a") as p: #Dados aleatorios em lista
        p.write(str(x))
        p.write('\n')
        p.close()


dict = {}
for i in range(len(x)):
    dict[x[i][0]] = x[i][1:]

######################################################################################

#######################################################################################
def example_arvore():
    valor = dict
    arvore = ArvoreBinariaBusca()
    for v in valor:
        arvore.insert(v)
    return arvore

#######################################################################################
print('\n---Ordem Simetrica---') # lista em ordem
abb = example_arvore()
abb.in_ordem_simetrica()
print('\n')

u = int(input("Digite: "))
items = [u] # a busca na nossa arvore
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
print ('Duracao Da Procura Na Arvore Binaria Ordem Simetrica: %f' % (fim - inicio))
    

#######################################################################################
print('\n----Ordem Aleatório---') # Orden que esta sendo inserida na arvore 
abb.percurso_nivel()
print("\n")

u = int(input("Digite: "))
items = [u] # a busca na nossa arvore
for elementos in items:
    r = abb.procurar(elementos) # metodo de busca na arvore
    if r is None:
        print(elementos, "Não encontrado")
        
    else:
        print(r.raiz.dado, 'encontrado')
        print(dict.get(u))

    #Contador de Doração da procura na arvore com valores aleatorios    
    time.sleep(1) #
inicio = timeit.default_timer()
fim = timeit.default_timer()
print ('Duracao Da Procura Na Arvore Binaria Ordem Aleatoria: %f' % (fim - inicio))
#######################################################################################

