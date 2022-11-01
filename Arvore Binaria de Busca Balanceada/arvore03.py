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


