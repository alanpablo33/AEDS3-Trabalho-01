class No: #classe que vai indicar os dados e direita esquesrda
    def __init__(self,dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self): #converter um No em str
        return str(self.dado)  #retorna o dado em forma de str

class ArvoreBinaria: #arvore 
    def __init__(self,dado=None):
        if dado:
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
    def percurso_pos_ordem(self, no=None,):
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
        


def pos(): # elementos da arvore
    arvore = ArvoreBinaria()
    n1 = No('I')
    n2 = No('N')
    n3 = No('S')
    n4 = No('C')
    n5 = No('R')
    n6 = No('E')
    n7 = No('V')
    n8 = No('A')
    n9 = No('5')
    n0 = No('3')

    n0.esquerda = n6
    n0.direita = n9
    n6.esquerda = n1
    n6.direita = n5
    n5.esquerda = n2
    n5.direita = n4
    n4.direita = n3
    n9.esquerda = n8
    n8.direita = n7

    arvore.raiz = n0
    return arvore

if __name__== "__main__":
    arvore = pos() # variavel com elementos da pos
    print("Percurso em pós ordem")
    arvore.percurso_pos_ordem() # passando def pos > percurso pos ordem
    print("Altura: ", arvore.altura())