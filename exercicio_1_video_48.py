nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
quantidade_de_caracteres_nome = len(nome)
if nome != "" and idade != "":
    print(f'Seu nome é: {nome}.')
    print(f'Seu nome invertido é: {nome[::-1]}.')
    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    print(f'Seu nome tem {quantidade_de_caracteres_nome} caracteres.')
    print(f'A primeira letra do seu nome é: {nome[0]}.')
    print(f'A última letra do seu nome é: {nome[quantidade_de_caracteres_nome-1]}.')
else:
    print('Desculpe, você deixou campos vazios.')