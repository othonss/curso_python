#Tem que ser com duas barra invertida para o python entender que é uma barra normal, ou seja, a barra invertida é um caractere de escape, então para usar a barra normal, tem que usar duas barras invertidas.
caminho_arquivo = 'C:\\Users\\othon\\OneDrive\\Área de Trabalho\\curso_python\\criando_arquivos_com_python\\'
caminho_arquivo += 'arquivo_criado.txt'

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá, este é um arquivo criado com Python!')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # O método writelines() escreve uma lista de strings no arquivo, sem adicionar quebras de linha automaticamente, por isso é necessário incluir '\n' no final de cada string para garantir que cada linha seja escrita em uma nova linha no arquivo.
    arquivo.writelines(['Linha 3\n', 'Linha 4\n', 'Linha 5\n'])

with open(caminho_arquivo, 'r') as arquivo:
    print('Lendo o arquivo criado:')
    conteudo = arquivo.read()
    print(conteudo)