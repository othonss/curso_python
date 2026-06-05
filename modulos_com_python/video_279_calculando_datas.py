from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

formato = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('03/10/1995 10:00:00', formato)
data_fim = datetime.strptime('05/06/2026 10:25:00', formato)

#Diferença total entre duas datas
delta = data_fim - data_inicio
print(delta.days, delta.seconds)
print(delta.total_seconds())

#É possível adicionar ou subtrair dias e horas com o timedelta
delta = timedelta(days=10, hours=2)
print(data_fim + delta)
print(data_fim - delta)

#Com um módulo a parte (relativedelta) é possível fazer outras contas
print(data_fim)
print(data_fim + relativedelta(seconds=60))

#É possível saber com o relativedelta mais detalhes das diferenças de datas
delta_detalhado = relativedelta(data_fim, data_inicio)
print(delta_detalhado)
#Pode ser mais específico também
print('Dias:',delta_detalhado.days, 'Anos:',delta_detalhado.years)
