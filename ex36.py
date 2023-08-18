valorCasa = float(input("Qual o valor da casa?"))
salarioComprador = float(input("Qual o salario do comprador?"))
quantidadeAnos = float(input("Em quantos anos ele vai pagar?"))

valorPrestacaoMensal = valorCasa / (quantidadeAnos)/12;

print("valorPrestacaoMensal: ", valorPrestacaoMensal)

if valorPrestacaoMensal > (salarioComprador * 0.30):
    print("O empréstimo vai ser negado")
else: 
    print("Tá tudo certo")   