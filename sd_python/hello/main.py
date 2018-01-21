import national_holiday
import datetime

jp_holidays = national_holiday.jp.NationalHoliday()
d = datetime.datetime.strptime('2018-05-03', '%Y-%m-%d').date()
print(d, jp_holidays.is_holiday(d))