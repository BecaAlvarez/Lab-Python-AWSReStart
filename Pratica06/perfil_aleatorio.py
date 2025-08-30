"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests
def obter_usuario():
    url = 'https://randomuser.me/api/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']}{dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}, email: {email}, pais = {pais}"

    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"

def main():
    print("Gerando um usuário aleatório...")
    usuario = obter_usuario()
    print(usuario)

if __name__ == "__main__":
    main()



