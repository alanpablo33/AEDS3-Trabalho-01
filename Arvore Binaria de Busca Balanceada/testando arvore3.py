import random
from arvore03 import ArvoreBinariaBusca

random.seed(77)

valor = random.sample(range(1,100),42)

bst= ArvoreBinariaBusca()
for v in valor:
    bst.insert(v)

bst.in_ordem_simetrica() # coloca em ordem simetrica 

print("\n")
items = [0,3,4,23,77,80] # a busca na nossa arvore
for elementos in items:
    r = bst.procurar(elementos)
    if r is None:
        print(elementos, "Não encontrado")
    else:
        print(r.raiz.dado, 'encontrado')