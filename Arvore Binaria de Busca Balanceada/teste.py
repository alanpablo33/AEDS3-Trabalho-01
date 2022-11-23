
#minha_lista = [
#     ['embu', '120', '910', '15', '1653', '9937'],
#     ['sao_paulo','456','123','9222','8933','8448'],
#     ['minas_gerais','1','2','10','99']
#]


#dict = {}
#for i in range(len(minha_lista)):
#    dict[minha_lista[i][0]] = minha_lista[i][1:]

#print(dict)
#print('\n')

#valoor = dict.get('embu')
#print(valoor)

def extractDigits(lst): 
    res = [] 
    for el in lst: 
        sub = el.split(', ') 
        res.append(sub) 
      
    return(res) 
                  
lst = ['alice, bob', 'cara'] 
print(extractDigits(lst)) 