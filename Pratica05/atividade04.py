"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
from datetime import date

def calcular_idade(ano_nasc):
    ano_atual = date.today().year
    idade_dias = (ano_atual - ano_nasc) * 365
    return idade_dias




while True:

    try:
        ano_nasc = int(input("Qual o ano que voce nasceu: "))
        idade_final = calcular_idade(ano_nasc)

    except ValueError:
        print("Digite um valor valido em inteiro")

    finally:
        print(f"Sua idade em dias é de {idade_final}")
        break