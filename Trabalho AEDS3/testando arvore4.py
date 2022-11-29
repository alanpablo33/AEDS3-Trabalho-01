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
    with open("DADOS.txt", "r") as arquivo: #converte para lista
        teste = arquivo.readlines()
        print(teste)
        print('\n')
        
    valor = teste
    arvore = ArvoreBinariaBusca()
    for v in valor:
        arvore.insert(v)
    return arvore

print('\n---Ordem Simetrica---')
abb = example_arvore()
abb.in_ordem_simetrica()
print('\n')

print('\n----Ordem Aleatório---')
abb.percurso_nivel()
print('\n')



items = input("Procure: ") # a busca na nossa arvore
for elementos in items:
    r = abb.procurar(elementos)
    if r is None:
        print(elementos, "Não encontrado")
    else:
        print(r.raiz.dado, 'encontrado')

