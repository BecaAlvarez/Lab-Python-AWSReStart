"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""
import csv

arquivo = "dados.csv"


def escrever_csv(dados, mode):

    try:
        with open(arquivo, mode, newline="", encoding="utf-8-sig") as arquivo_csv:
            escritor = csv.writer(arquivo_csv, delimiter=";")

            if mode == "w":
                escritor.writerow(["Nome", "Idade", "Cidade"])

            escritor.writerows(dados)
        print(f"Arquivo '{arquivo}' atualizado com sucesso!")

    except FileNotFoundError:
        print("Arquivo não encontrado!")


if __name__ == "__main__":
    nome = input("Digite o nome: ").strip()
    idade = input("Digite a idade: ").strip()
    cidade = input("Digite a cidade: ").strip()

    dados = [[nome, idade, cidade]]

    while True:

        try:
            resp = int(input("Digite a opção desejada: 1 - Acrescentar registro  2 - Sobrescrever registro 3 - Sair: "))

            if resp == 1:
                escrever_csv(dados, "a")
                break
            elif resp == 2:
                escrever_csv(dados, "w")
                break
            elif resp == 3:
                print("PROGRAMA ENCERRADO!")
                break
            else:
                raise ValueError("Operação inválida. Digite somente valores 1, 2 ou 3")


        except ValueError:
            print("Operação inválida. Digite somente valores 1, 2 ou 3")
            continue



