while True:
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    numeros_validos = None

    try:
        x = float(numero1)
        y = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Valores digitados não válidos")
        continue
    else:  
        def soma(x, y):
            return x + y

    resultado = soma(x, y)
    print(f'{numero1} + {numero2} = ', resultado)
    break