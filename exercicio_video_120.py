def multiplicar_numero(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicar_numero(2)
triplicar = multiplicar_numero(3)
quadruplicar = multiplicar_numero(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
