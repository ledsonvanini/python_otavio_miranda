from datetime import datetime, timedelta

from modulos import pp, pl

data1 = datetime(1986,9,3)
data2 = datetime(2023,1,19)

time_delta = timedelta(days=23, hours=12)

# TimeDelta é a diferença entre duas datas
delta_time = data1 - data2  # Retorna um Deltatime em dias -13287 de onde se pode extrair Dias, min, sec horas etc
print(delta_time)
pl()
print(delta_time - time_delta)
print(dir(delta_time))