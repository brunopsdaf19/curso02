import random
lista = []
for contadora in range (1,100):
    aux = int(random.randint(0, 30))
    lista.append(aux)

print(lista)
print(f"\n")
print(f"Lista em ordem numerica: ")
print(sorted(lista))