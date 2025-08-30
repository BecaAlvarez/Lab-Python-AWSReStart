"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:


    Distância percorrida: 300 km

    Combustível gasto: 25 litros

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
def calcular_combustivel(km, litros):
    consumo_medio = km / litros
    return consumo_medio

while True:

    try:
        km = float(input("Informe a distância percorrida em km: "))
        litros = float(input("Informe a combustível gasto em litro(l): "))
        consumo_medio = calcular_combustivel(km, litros)
        print(f"""
        DADOS DE SUA VIAGEM
        Distância percorrida: {km}
        Combustível gasto: {litros}
        consumo médio (km/l): {consumo_medio:.2f}"
        """)
        break
    except  ValueError:
        print("Digite somente NÚMEROS REAIS")


