num = int(input("Digite um numero inteiro: "))
contador = 0
i = 10

resultado = num
for num in range(i): 
    contador += 1
    print(resultado , ' x ', contador, ' = ', resultado*contador)