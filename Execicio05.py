import random

lista = []
lista_impar = []
lista_par = []

for aux in range (1,101):
    lista.append(aux)

    if (aux % 2 == 0):
        lista_par.append(aux)
    if (aux % 2 == 1):
        lista_impar.append(aux)

print(lista)
print(f"A soma de todos os numero da lista {sum(lista)} ")
print(f"A media da lista {sum(lista) / len(lista):.2f} ")
print(f"A soma de todos os numero pares da lista {sum(lista_par)} ")
print(f"A soma de todos os numero impares da lista {sum(lista_impar)} ")
