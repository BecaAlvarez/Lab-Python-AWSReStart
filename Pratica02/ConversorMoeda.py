"""
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:


    Valor em reais: R$ 100.00

    Taxa do dólar: R$ 5.60

    Taxa do euro: R$ 6.60

O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

"""

real = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_convertido_dolar = real / taxa_dolar
valor_convertido_euro = real / taxa_euro

print(f"Conversão para dólar: {valor_convertido_dolar:.2f}")
print(f"Conversão para euro: {valor_convertido_euro:.2f}")

