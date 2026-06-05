from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('Asia/Tokyo'))
print(data)
# data_str_data = '2026/06/05 10:07:00'
# data_str_data = '05/06/2026'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2026, 6, 5, 10, 1, 00)
# data_formatada = datetime.strptime(data_str_data, data_str_fmt)
# print(data)
# print(data_formatada)