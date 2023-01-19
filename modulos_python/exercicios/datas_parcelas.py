
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
data_emprestimo = datetime(2020,12,20)
delta_anos = relativedelta(years=5)
data_final_emprestimo = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final_emprestimo:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

for d in data_parcelas:
    print(f'Parcela::{d}')

