import random

minhaEscolha = str(input("Digite sua escolha: "))

jokenpoList = ['pedra', 'papel', 'tesoura']

print(minhaEscolha)
print(random.choice(jokenpoList))

if minhaEscolha == random.choice(jokenpoList):
    print("empate")
elif minhaEscolha == 'pedra' and random.choice(jokenpoList) == 'papel':
    print("computador ganhou")
elif minhaEscolha == 'pedra' and random.choice(jokenpoList) == 'tesoura':
    print("eu ganhei")
elif minhaEscolha == 'tesoura' and random.choice(jokenpoList) == 'papel':
    print("eu ganhei")
