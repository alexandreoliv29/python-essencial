seg1 = float(input("primeiro segmento: "))
seg2 = float(input("segundo segmento: "))
seg3 = float(input("terceiro segmento: "))

""" Cada segmento tem que ser menor que a soma dos outros dois para ser possível formar um triângulo"""

if(seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2):
    print("e um triangulo")
else:
    print(" nao e um triangulo")