"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).
"""

idade = int(input("Qual a sua idade: "))


if idade <= 12:
    print("Classificação: Criança")
elif 12 < idade <= 17:
    print("Classificação: Adolescente")
elif 17 < idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")