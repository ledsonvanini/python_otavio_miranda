from datetime import datetime

frmt = '%d/%m/%Y'

data = datetime(2023,1,19)
data_1 = datetime.strptime('2023-1-19 07:59:17', '%Y-%m-%d %H:%M:%S')

data_2 = data_1.strftime(frmt)

print(data_1.strftime('%d/%m/%Y'))
print(data_1.strftime('%d'), data_1.day)
print(data_1.strftime('%m'), data_1.minute)
print(data_1.strftime('%Y'), data_1.year)

print(data_1)
print(data_2)
