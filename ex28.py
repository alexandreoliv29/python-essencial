import random

list = [1,2,3,4,5]
numComputador = random.choice(list)

numUsuario = int(input("Digite o numero que o computador pensou: "))

print("numComputador: ", numComputador)
print("numUsuario: ", numUsuario)


if numUsuario == numComputador:
    print("voce acertou!")
else: print("voce errou!")