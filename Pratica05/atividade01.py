"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
    Retorna: float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem):
    valor_desconto = valor_conta * (porcentagem / 100)
    valor_final = valor_conta + valor_desconto
    return valor_final


valor_conta = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a somente o valor porcentagem da gorjeta: "))

valor_conta = calcular_gorjeta(valor_conta, porcentagem)
print(f"Valor da conta somado a gorjeta: {valor_conta:.2f}")