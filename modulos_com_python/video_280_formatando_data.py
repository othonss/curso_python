from datetime import datetime

formato_apenas_data = '%d/%m/%Y'
formato_data_hora = '%d/%m/%Y %H:%M'
formato_apenas_ano = '%Y'

data = datetime.strptime('2026-06-05 10:51:00', '%Y-%m-%d %H:%M:%S')
print(data.strftime(formato_apenas_data))
print(data.strftime(formato_data_hora))
print(data.strftime(formato_apenas_ano))
#Pode ser direito no print também
print(data.strftime('%m/%Y')) #Neste caso, mês e ano