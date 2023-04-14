print("Primeira pessoa")
nome = input("Nome: ")
altura = float(input("Diga sua altura: "))
peso = int(input("Seu Peso"))
print("\nSegunda pessoa")
nome2 = input("Nome: ")
altura2 = float(input("Diga su altura: "))
peso2 = int(input("Seu peso: "))


if(altura > altura2):
    print(f"O {nome} é mais alto")
else:
    maioraltura = altura2
    print(f"O {nome2} é mais alto ")
if(peso > peso2):
    print(f"O {nome} é mais pesado ")
else:
    print(f"O {nome2} é mais pesado")




