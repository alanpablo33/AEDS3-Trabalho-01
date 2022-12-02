
minha_lista = [
     [100, 120, 'Alan'],
     [200,456,'pablo'],
     [300,1,'alves']
]

dict = {}
for i in range(len(minha_lista)):
    dict[minha_lista[i][0]] = minha_lista[i][1:]


#v= dict.get(100)
#print(v)

print(dict)
dados1 = []

dados1.append({
            'chave': dict,           
         })

#with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
#        for l1 in dados1:
#            arquivo.write(f'  {l1["chave"]} ')
#            arquivo.write('\n')
#            print("\n")

#with open("DADOS.txt", "r") as arquivo: #ler o txt
#        teste = arquivo.readlines()
#        dict = {}
#for i in range(len(teste)):
#    dict[teste[i][0]] = teste[i][1:]
#    print('\n')
#    print(teste)

###########################################

#mydict = {}
#mydict['item'] = 1
#print(mydict)

#dados1.append({
#            'chave': key,
#            'valor_inteiro': valores_inteiros,
#            'char_1000':char 
#         })

#with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
#        for l1 in dados1:
#            arquivo.write(f' CHAVE: {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]} CHAR: {l1["char_1000"]}')
#            arquivo.write('\n')

#with open('DADOS2.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
#        for l1 in dados1:
#            arquivo.write(f' CHAVE: {l1["chave"]}  : VALOR INTEIRO: {l1["valor_inteiro"]} CHAR: {l1["char_1000"]}')
#            arquivo.write('\n')


#with open("DADOS2.txt", "r") as arquivo: #ler o txt
#        teste = arquivo.readlines()
#        w= random.sample(teste,len(teste)) #valores do arquivo txt DADOS2 aleatorios
#        print('\n')


import time
import timeit


def alguma_funcao():
    for i in range(1, 5):
        time.sleep(1)

inicio = timeit.default_timer()
alguma_funcao()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))


#dados1 = [] # AQUI ESTA O PROBLEMA!!!!!!!!!!!!!!!!

#dados1.append({
#            'chave': resultados,
#            
#         })

#with open('DADOS.txt', 'a') as arquivo: # ENVIANDO TUDO PARA O ARQUIVO TXT
#        for l1 in dados1:
#            arquivo.write(f' {l1["chave"]} ')
#            arquivo.write('\n')
#            print("\n")

#with open("DADOS.txt", "r") as arquivo: #ler o txt
#        teste = arquivo.readlines()
#        print(teste)



