"""
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada: O arquivo de entrada contém 4 valores inteiros.
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

var_a = int(input("Digite o valor para 'A': "))
var_b = int(input("Digite o valor para 'B': "))
var_c = int(input("Digite o valor para 'C': "))
var_d = int(input("Digite o valor para 'D': "))

diferenca = (var_a * var_b - var_c * var_d)

print("Diferença do produto de A e B pelo produto de C e D")
print(f"DIFERENCA = {diferenca}")