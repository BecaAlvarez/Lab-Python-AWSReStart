"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:

    Permitir que o usuário informe o preço do produto e o percentual de desconto.
    Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
    Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""
def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

preco = float(input("Insira o preço do produto: "))
percentual = float(input("Insira o percentual do desconto: "))

preco = calcular_desconto(preco, percentual)
print(f"O preço final com desconto é {preco:.2f}")