import requests

def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            return "CEP não encontrado."

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("estado", "Não informado")

        return f"\nCEP: {cep}\nLogradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"

    except requests.RequestException as e:
        return f"Erro na consulta: {e}"

def main():
    while True:
        cep = input("Informe o CEP para consulta (somente números): ")
        if len(cep) == 8:
            endereco = busca_cep(cep)
            print(endereco)
            break
        print("O CEP digitado não contêm 8 digitos. Tente novamente")


if __name__ == "__main__":
    main()
