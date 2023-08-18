anoNascimento = int(input("Qual o ano do seu nascimento? "))

idade = 2023 - anoNascimento

if idade == 18:
    print("Esta na hora de se alistar")
elif idade > 18:
    print("ja passou do tempo de alistamento")
else: 
    print("Ainda vai se alistar")
