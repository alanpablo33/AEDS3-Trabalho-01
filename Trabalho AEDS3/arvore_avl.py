# import random, math
from fila import Fila # importação de fila
from palavras import palavras # Modulo com palavras aleatorias
import random # função aleatorio
import time
import timeit



debugEnable = True

def debug(string):
    if debugEnable is True:
        print(string)


class Node():
    # Construtor do Nó
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

    def __str__(self):
        return "{ '" + str(self.key) + "' : " + str(self.data) + " }"

    def getBalance(self):
        if self.left and self.right:
            return AVLTree.update_heights(self, True)


class AVLTree():
    # Construtor da Árvore
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node
        newnode = Node(key, [])

        # Se a árvore for vazia, realizar a primeira inserção
        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Nó (" + str(key) + ") inserido")

        # Se a chave for menor, procurar nas subárvores a esquerda
        elif key < tree.key:
            self.node.left.insert(key)

        # Se a chave for maior, procurar nas subárvores a direita
        elif key > tree.key:
            self.node.right.insert(key)

        # Se a chave já existir na árvore
        else:
            debug("Nó (" + str(key) + ") já existe na árvore.")

        # Realiza o balanceamento da árvore, se necessário
        self.rebalance()

    def rebalance(self):
        # Realiza o balanceamento da árvore inteira
        self.update_heights(False)
        self.update_balances(False)

        # Verifica se o fator de balanceamento é maior que 1 ou menor que -1
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()        # Rotação para a esquerda no filho a esquerda (casos de joelho)
                    self.update_heights()
                    self.update_balances()
                self.rrotate()                      # Rotação para a direita no nó, para valor positivo de FB
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()       # Rotação para a direita no filho a direita (casos de joelho)
                    self.update_heights()
                    self.update_balances()
                self.lrotate()                      # Rotação para a esquerda no nó, para valor negativo de FB
                self.update_heights()
                self.update_balances()

    # Rotação a direita
    def rrotate(self):
        debug('Rotacionando ' + str(self.node.key) + ' para a direita')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    # Rotação a esquerda
    def lrotate(self):
        debug('Rotacionando ' + str(self.node.key) + ' para a esquerda')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    # Função recursiva para atualizar a altura de cada nó
    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        # Se não houver nó
        else:
            self.height = -1

    # Função recursiva para atualizar o balanceamento de cada nó
    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
            return self.balance
        else:
            self.balance = 0
            return self.balance

    def delete(self, key):
        if self.node != None:
            if self.node.key == key:
                debug("Removendo: " + str(key))
                # Se o nó for uma folha, simpelsmente remover.
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None
                # Se o nó tiver não tiver um filho a esquerda, mas tiver o da direita, tornar o filho a direita a raíz
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                # Se o nó tiver não tiver um filho a direita, mas tiver o da esquerda, tornar o filho a esquerda a raíz
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # Caso não seja nenhum dos casos acima, devolver o nó sucessor.
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # Verifica se o nó para substituir não é vazio
                        debug("Substituindo " + str(key) + " por " + str(replacement.key))
                        self.node.key = replacement.key
                        self.node.right.delete(replacement.key)

                # Chama a função para rebalancear árvore
                self.rebalance()
                return

            # Se não for o nó desejado, procurar nas suas sub-árvores
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    # Retorna o predecessor lógico
    def logical_predecessor(self, node):
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    # Retorna o sucessor lógico
    def logical_successor(self, node):
        node = node.right.node
        if node != None:
            while node.left != None:
                debug("Procurando sucessor. Atual: " + str(node.key))
                if node.left.node == None:
                    debug("Fim da pesquisa de nó sucessor. Encontrado: " + str(node.key))
                    return node
                else:
                    node = node.left.node
        return node

    # Verifica se a árvore está balanceada
    def check_balanced(self):
        if self == None or self.node == None:
            return True
        self.update_heights()
        self.update_balances()
        ## ABS: retorna o valor absoluto. Verifica se a função está balanceada, retornando "false" caso não.
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    # Preenche um vetor com as chaves em-ordem.
    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist
    
    def procura(self, key):
        tree = self.node

        # Se a chave for menor, procurar nas subárvores a esquerda
        if key < tree.key:
            self.node.left.procura(key)

        # Se a chave for maior, procurar nas subárvores a direita
        elif key > tree.key:
            self.node.right.procura(key)
        
        # Se a chave já existir na árvore
        else:
            debug("Nó (" + str(key) + ") Encontrado Na Arvore.")

####################################################################################################
#INICIO 

cont = 1000 # quantidade de elementos criados

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
   print("\n")
elemento = random.shuffle(resultados) # bagunça na lista
dict = {}
for i in range(len(resultados)):
    dict[resultados[i][0]] = resultados[i][1:]

######################################################################################

def example_arvore():
    inlist = dict
    arvore = AVLTree()
    for i in inlist:
        arvore.insert(i)
    return arvore

print("\n\n")
abb = example_arvore()
print("\n\n")

abb.procura(int(input("Digite o Valor a Buscar: "))) #Buscando valor na arvore
time.sleep(1) #
inicio = timeit.default_timer()
fim = timeit.default_timer()
print ('Duracao Da Procura Na Arvore Binaria Ordem Aleatoria: %f' % (fim - inicio))
 

        

