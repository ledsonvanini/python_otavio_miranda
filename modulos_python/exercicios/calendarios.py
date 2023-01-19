
import calendar
from calendar import TextCalendar

calendario_2022 = calendar.calendar(2022)

# Explorando dias do mes list()
def get_weeks(year=2023, month=1):
    print(f'0{month}/{year}')
    for week in calendar.monthcalendar(year, month):
        print(week)
    print(30 * '*')

get_weeks()
get_weeks(2023, 5)


# # print(calendario_2022)
# print(calendar.month(2022, 9))
# print(calendar.monthrange(2023,2))
# print(calendar.day_name[2])
# print(list(calendar.day_name))
