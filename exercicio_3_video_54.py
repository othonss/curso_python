nome = input('Informe o primeiro nome: ')
quantidade_caracteres_nome = len(nome)
if nome.isnumeric():
    print('Por favor escreva o seu nome corretamente, usando apenas letras')
elif quantidade_caracteres_nome !=0 and quantidade_caracteres_nome <= 4:
    print('Seu nome é curto')
elif quantidade_caracteres_nome >= 5 and quantidade_caracteres_nome <= 6:
    print('Seu nome é normal')
elif quantidade_caracteres_nome > 6:
    print('Seu nome é muito grande')
else:
    print('Preencha o campo')