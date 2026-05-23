cpf = input('Informe o CPF: ')

digitos_numericos = []
soma_digitos_necessarios_1 = 0
soma_digitos_necessarios_2 = 0
multiplicador_digito_1 = 10
multiplicador_digito_2 = 11

for digito in cpf:
    if digito.isnumeric():
        digitos_numericos.append(digito)

#Digito um
for indice, digito in enumerate(digitos_numericos):
    digito = int(digito)
    soma_digitos_necessarios_1 += digito * multiplicador_digito_1
    multiplicador_digito_1 = multiplicador_digito_1 -1
    if multiplicador_digito_1 < 2:
        multiplicador_digito_1 = 0

resto_digitos_multiplicados_1 = (soma_digitos_necessarios_1 * 10) % 11
resultado_digito_1 = resto_digitos_multiplicados_1 if resto_digitos_multiplicados_1 <= 9 else 0

#Digito dois
for indice, digito in enumerate(digitos_numericos):
    if indice == 9:
        digitos_numericos[indice] = resultado_digito_1
    digito = int(digito)
    soma_digitos_necessarios_2 += digito * multiplicador_digito_2
    multiplicador_digito_2 = multiplicador_digito_2 -1
    if multiplicador_digito_2 < 2:
        multiplicador_digito_2 = 0

resto_digitos_multiplicados_2 = (soma_digitos_necessarios_2 * 10) % 11
resultado_digito_2 = resto_digitos_multiplicados_2 if resto_digitos_multiplicados_2 <= 9 else 0

if cpf[12] != str(resultado_digito_1) or cpf[13] != str(resultado_digito_2):
    print('CPF inválido!')
else:
    print('CPF Válido')
    
print('Digitos finais do CPF: ', resultado_digito_1, resultado_digito_2)