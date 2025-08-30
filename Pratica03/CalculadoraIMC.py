"""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

"""
peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))


imc = peso / (altura ** 2)

if imc < 18.5:
    print("classificacao = Abaixo do peso")
elif 18.5 < imc < 25:
    print("classificacao = Peso normal")
elif 25 < imc < 30:
    print("classificacao = Sobrepeso")
else:
    print("classificacao = Obeso")