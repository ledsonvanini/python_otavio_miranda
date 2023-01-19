
""""""
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

data = datetime(2023, 1, 19, tzinfo=timezone('Asia/Tokyo'))
hora_atual = datetime.now(tz=timezone('America/Sao_Paulo'))  # 'America/Sao_Paulo' >>  (SP, RJ, GO, DF, MG, ES SC, PR, RS)
# data_atual = datetime.now('Asia/Tokyo')  Exemplo

print(hora_atual) # UTC 03 Sao Paulo
print(data)  # UTC-09 Asia