"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL).
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual,
máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import datetime
import requests
def conversao_moeda(cod_moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{cod_moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()[f"{cod_moeda}BRL"]
        valor_atual = float(dados["bid"])
        min_contacao = float(dados["low"])
        max_cotacao = float(dados["high"])
        date_hour = dados["create_date"]
        return f"""
        CONVERSÃO DO {cod_moeda} PARA BRL
        _________________________________
        Valor atual: R${valor_atual:.2f}
        Valor mínimo: R${min_contacao:.2f}
        Valor máximo: R${max_cotacao:.2f}
        Data e hora: {date_hour}
        """

    except requests.RequestException as e:
        print(f"Error: {e}")

cod_moeda = str(input(f"Digite o codigo da moeda que deseja converter: ")).upper().strip()
infor = conversao_moeda(cod_moeda)
print(infor)
