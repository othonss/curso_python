hora = input('Informe qual é o horário atual (apenas a hora, ex: se for 13h30 então informe somente 13): ')

try:
    hora_convertida_int = int(hora)
    if hora_convertida_int >= 0 and hora_convertida_int <= 5:
        print('Boa madrugada!')
    elif hora_convertida_int >= 6 and hora_convertida_int <= 11:
        print('Bom dia!')
    elif hora_convertida_int >= 12 and hora_convertida_int <= 17:
        print('Boa tarde!')
    elif hora_convertida_int >= 18 and hora_convertida_int <= 23: 
        print('Boa noite!')
    else:
        print('Informe um horário correto (0 a 24)')
except:
    print('Informe um valor correto!')