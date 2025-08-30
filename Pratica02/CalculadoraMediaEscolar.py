"""
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:


    Nota 1: 7.5

    Nota 2: 8.0

    Nota 3: 6.5

O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

media = calcular_media(nota1, nota2, nota3)
print(f"\nCalcular a média escolar de aluno")
print(f"\nResultado final: {media:.2f}")