"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes.
"""
import json
import math

arquivo = "logs.json"

def ler_arquivo(arquivo):

    try:
        with open(arquivo, 'r') as file:
            logs = json.load(file)
            return logs

    except FileNotFoundError:
        return f"Arquivo não encontrado"


def calculo_ml(arquivo):

    try:
        dados = ler_arquivo(arquivo)
        tempos = [item["tempo_execucao"] for item in dados]
        n = len(tempos)
        #Média
        media = sum(tempos) / n
        # Desvio padrão
        desvio_pop = math.sqrt(sum((x - media) ** 2 for x in tempos) / n)
        print(f"Média do tempo: {media} / Desvio padrão do tempo de exercução constantes: {desvio_pop}")
    except Exception:
        print(f"Erro calcular os logs")


if __name__ == '__main__':
    logsML = ler_arquivo(arquivo)
    print(10*"*"+ " LOGS DE TREINAMENTO " + 10*"*")
    print(logsML)
    print(10 * "*" + " CALCULOS " + 10 * "*")
    calculo_ml(arquivo)


