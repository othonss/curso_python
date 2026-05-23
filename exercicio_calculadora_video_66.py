while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    numero_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os valores digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos or len(operador) > 1:
        print('Aceita só um operador por vez entre, sendo eles: (* multiplicação), (/ divisão), (+ adição) e (- subtração).')
        continue    

    if operador == '+':
        print(f'[ADIÇÃO] {num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'[SUBTRAÇÃO] {num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'[DIVISÃO] {num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'[MULTIPLICAÇÃO] {num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    #Vai pegar o input, colocar tudo em minusculo e verificar se começa com "s", retornando um bool
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break