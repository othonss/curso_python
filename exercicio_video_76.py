import os

palavra_secreta = 'python'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_entrada_usuario = input('Digite uma letra: ')
    palavra_formada = ''
    numero_tentativas += 1

    if len(letra_entrada_usuario) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_entrada_usuario in palavra_secreta:
        letras_acertadas += letra_entrada_usuario

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra secreta era: ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
