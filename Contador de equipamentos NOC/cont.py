#Contador de Portas e Equipamentos em OLT-Alan_Boladão

def conta_itens(onu):
  quantidade = 0
  for item in onu:
    if "-" in item:
       quantidade = quantidade + soma_partes(item)
       continue
    quantidade = quantidade + 1
    
  return quantidade

def soma_partes(onu_item):
  partes = onu_item.split("-")
  parte_1 = int(partes[0])
  parte_2 = int(partes[1])
  return parte_2 - parte_1 + 1

onu = []
onu.append(input("Insira aqui os Valores: "))

print(conta_itens(onu))

