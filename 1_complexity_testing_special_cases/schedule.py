import datetime


def analyze(year, holiday_dates, first_day):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_per_year = [0] * 7
    holidays_per_weekday = [0] * 7
    month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    days_in_year = 366 if is_leap else 365

    first_day_number = days.index(first_day)

    for i in range(7):
        if i == first_day_number:
            weekdays_per_year[i] += days_in_year // 7 + 1
        else:
            weekdays_per_year[i] += days_in_year // 7

    for holiday in holiday_dates:
        day = int(holiday[0])
        month = holiday[1]
        holiday_date = datetime.date(year, month_dict[month], day)
        day_of_week = holiday_date.weekday()
        holidays_per_weekday[day_of_week] += 1

    number_of_holidays_per_choice = {day: 0 for day in days}
    for day in range(7):
        number_of_holidays_per_choice[days[day]] += weekdays_per_year[day]
        for j in range(7):
            if day != j:
                number_of_holidays_per_choice[days[day]] += holidays_per_weekday[j]

    print(max(number_of_holidays_per_choice, key=number_of_holidays_per_choice.get), min(number_of_holidays_per_choice, key=number_of_holidays_per_choice.get))


input_n = int(input())
input_year = int(input())
input_holiday_dates = [list(map(str, input().split())) for _ in range(input_n)]
input_first_day = input()
analyze(input_year, input_holiday_dates, input_first_day)
