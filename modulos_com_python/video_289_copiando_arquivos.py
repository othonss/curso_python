import os
import shutil

HOME = os.path.expanduser('~')
PASTA_ORIGINAL = os.path.join(HOME, 'EXEMPLO')
NOVA_PASTA = os.path.join(HOME, 'NOVA_PASTA')
print(NOVA_PASTA)

#Criando uma nova pasta
os.makedirs(NOVA_PASTA, exist_ok=True)

#Fazendo um loop para ver cada o conteúdo da pasta
for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
