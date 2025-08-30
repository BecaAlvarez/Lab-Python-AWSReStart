"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
def is_palindromo(palavra):
    palavra_limpa = ''.join((palavra.split()))
    new_palavra = palavra_limpa[::-1]
    if new_palavra == palavra_limpa:
        return f"A palavra é um palíndromo"
    else:
        return f"A palavra não é um palíndromo: {new_palavra}"



palavra = str(input("Digite uma palavra para verificar se é palíndromo: ")).lower()
nova_palavra = is_palindromo(palavra)
print(nova_palavra)