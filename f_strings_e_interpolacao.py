nome = "Othon"
altura = 1.80
peso = 60
imc = peso / (altura * altura)

#Formatação com a função format
resultado = '{nome} tem {altura:.2f} de altura, pesa {peso:.2f} quilos e seu IMC é {imc:.2f}'
print(resultado.format(nome=nome, altura=altura, peso=peso, imc=imc))
#Formatação com f-strings
print(f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f} quilos e seu IMC é {imc:.2f}')
#Interpolação de strings
print('%s tem %.2f de altura, pesa %.2f quilos e seu IMC é %.2f' % (nome, altura, peso, imc))
