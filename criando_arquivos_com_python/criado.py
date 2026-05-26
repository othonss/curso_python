#Tem que ser com duas barra invertida para o python entender que é uma barra normal, ou seja, a barra invertida é um caractere de escape, então para usar a barra normal, tem que usar duas barras invertidas.
caminho_arquivo = 'C:\\Users\\othon\\OneDrive\\Área de Trabalho\\curso_python\\criando_arquivos_com_python\\'
caminho_arquivo += 'arquivo_criado.txt'

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá, este é um arquivo criado com Python!')
