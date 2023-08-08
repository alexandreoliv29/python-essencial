import math

catetoOposto = float(input("Digite o comprimento do cateto oposto: "))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(catetoOposto**2 * catetoAdjacente**2)

print("a hipotenusa e: ", hipotenusa)
