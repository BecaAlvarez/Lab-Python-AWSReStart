"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

Fórmulas de Conversão
Celsius para Fahrenheit: °F = (°C × 9/5) + 32
Celsius para Kelvin: K = °C + 273.15
Fahrenheit para Celsius: °C = (°F - 32) × 5/9
Fahrenheit para Kelvin: K = (°F - 32) × 5/9 + 273.15
Kelvin para Celsius: °C = K - 273.15
Kelvin para Fahrenheit: °F = (K - 273.15) × 9/5 + 32
"""

def celsius_to_fahrenheit(c): return (c * 9/5) + 32

def celsius_to_kelvin(c): return c + 273.15

def fahrenheit_to_celsius(f): return (f - 32) * 5/9

def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k): return k - 273.15

def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

def conversao_temp(unidade_origem, unidade_conversao):
    if unidade_origem == 1:
        if unidade_conversao == 2:
            temperatura_convertida = celsius_to_fahrenheit(temperatura)
            print(f"{temperatura}°C = {temperatura_convertida}°F")
        elif unidade_conversao == 3:
            temperatura_convertida = celsius_to_kelvin(temperatura)
            print(f"{temperatura}°C = {temperatura_convertida}K")
    elif unidade_origem == 2:
        if unidade_conversao == 1:
            temperatura_convertida = fahrenheit_to_celsius(temperatura)
            print(f"{temperatura}°F = {temperatura_convertida}°C")
        elif unidade_conversao == 3:
            temperatura_convertida = fahrenheit_to_kelvin(temperatura)
            print(f"{temperatura}°F = {temperatura_convertida}K")
    elif unidade_origem == 3:
        if unidade_conversao == 1:
            temperatura_convertida = kelvin_to_celsius(temperatura)
            print(f"{temperatura}K = {temperatura_convertida}°C")
        elif unidade_conversao == 2:
            temperatura_convertida = kelvin_to_fahrenheit(temperatura)
            print(f"{temperatura}K = {temperatura_convertida}°F")
    else:
        print("Sem entrada ou opção inexistente!")




print("Conversor de Temperatura")
temperatura = float(input("Informe a temperatura: "))

print("Digite o número da opção desejada")
print("1: Celsius, 2: Fahrenheit, 3: Kelvin")

unidade_origem = int(input("Informe a unidade de origem: "))
unidade_conversao = int(input("Informe a unidade para qual deseja converter: "))

conversao_temp(unidade_origem, unidade_conversao)




