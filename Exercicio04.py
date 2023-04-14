print("Considere a estação prevalente para cada mês: ")
print("(1)Janeiro")
print("(2)Fevereiro")
print("(3)Março")
print("(4)Abril")
print("(5)Maio")
print("(6)Junho")
print("(7)Julho")
print("(8)Agosto")
print("(9)Setembro")
print("(10)Outubro")
print("(11)Novembro")
print("(12)Dezembro")

estacoes = int(input("Escolha o mes que deseja: "))

if(estacoes == 1 or estacoes == 2 or estacoes == 3):
    print(f"A estação do ano correspondente ao mes {estacoes} é Verão")
elif(estacoes == 4 or estacoes == 5 or estacoes == 6):
    print(f"A estação do ano correspondente ao mes {estacoes} é Outono")
elif(estacoes == 7 or estacoes == 8 or estacoes == 9):
    print(f"A estação do ano correspondente ao mes {estacoes} é Inverno")
elif(estacoes == 10 or estacoes == 11 or estacoes == 12):
    print(f"A estação do ano correspondente ao mes {estacoes} é Primavera")
else:
    print("Numero invalido")