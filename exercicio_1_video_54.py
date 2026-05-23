numero = input('Digite um número inteiro: ')

try:
    int_numero = int(numero)
    print('Cheguei aqui')
    if int_numero % 2 == 0:
        print('O número digitado é par!')
    else:
        print('O número digitado é impar!')
except:
    print('O número digitado não se trata de um inteiro.')