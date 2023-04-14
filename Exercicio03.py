import random

lista = []
for contadora in range (1,20):
    aux = int(random.randint(0, 30))
    lista.append(aux)

print(lista)
print(f" O maior numero da lista é {max(lista)}")
print(f"O menor numero da lista é {min(lista)}")