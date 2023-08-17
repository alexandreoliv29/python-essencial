velocidade = int(input("Digite a velocidade do carro: "))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print("voce foi multado em {}".format(multa))
else: 
    print("deu sorte")
