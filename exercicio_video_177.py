lista1 = [1, 2, 3]
lista2 = [6, 7, 8, 9, 10]

#Minha lógica
novalista = []

menor_lista = min(len(lista1), len(lista2))
for i in range(menor_lista):
    novalista.append((lista1[i] + lista2[i]))
print(novalista) 

#Lógica do professor
lista_soma = [x + y for x, y in zip(lista1, lista2)]
print(lista_soma)