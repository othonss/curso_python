from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'video_296_csv.csv'

#Forma de leitura padrão
# with open(CAMINHO_CSV, 'r', encoding='UTF-8') as arquivo:
#     leitor = csv.reader(arquivo)
#     for linha in leitor:
#         print(linha)

#Forma de leitura por dicionario
with open(CAMINHO_CSV, 'r', encoding='UTF-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])