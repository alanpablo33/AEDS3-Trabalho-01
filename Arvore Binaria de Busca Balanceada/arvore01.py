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
      


if __name__== "__main__":
    #arvore = ArvoreBinaria(7)
    #arvore.raiz.esquerda = No(18)
    #arvore.raiz.direita = No(14)

    #print(arvore.raiz)
    #print(arvore.raiz.esquerda)
    #print(arvore.raiz.direita)

    arvore = ArvoreBinaria()
    n1 = No('a')
    n2 = No('+')
    n3 = No('*')
    n4 = No('b')
    n5 = No('-')
    n6 = No('/')
    n7 = No('c')
    n8 = No('d')
    n9 = No('e')

    n6.esquerda = n7
    n6.direita = n8
    n5.esquerda = n6
    n5.direita = n9
    n3.esquerda = n4
    n3.direita = n5
    n2.esquerda = n1
    n2.direita = n3

    arvore.raiz = n2

    arvore.percurso_simetrico()
