#PERCURSO em NÍVEL em ÁRVORE BINÁRIA 

import random
from arvore04 import ArvoreBinariaBusca
from arquivosTXT import *

random.seed(77)

def random_arvore(size=42):
    valor = random.sample(range(1, 1000), 42)
    arvore = ArvoreBinariaBusca()
    for v in valor:
        arvore.insert(v)
    return arvore

def example_arvore():
#    with open("DADOS.txt", "r") as arquivo: #converte para lista
#        teste = arquivo.readlines()
#        print(teste)
#        print('\n')
        
    valor = [18,7,10,33,1,25,2]
    arvore = ArvoreBinariaBusca()
    for v in valor:
        arvore.insert(v)
    return arvore

print('\n---Ordem Simetrica---')
abb = example_arvore()
abb.in_ordem_simetrica()
print('\n')

print('\n----Ordem Por Nivel Do Primeiro para o Ultimo Nivel----')
abb.percurso_nivel()
print('\n')