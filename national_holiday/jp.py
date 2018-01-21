import pathlib
import datetime

class NationalHoliday():

    def __init__(self):
        self._holidays = None

    
    @property
    def holidays(self):
        if self._holidays is None:
            self._holidays = self.load_holidays()
        return self._holidays

    def load_holidays(self):
        holiday_dict = {}

        current_dir = pathlib.Path(__file__).resolve().parent
        holiday_file = current_dir / 'holiday_data' / 'jp.yml'

        with open(holiday_file, 'r') as f:
            for line in f:
                day, holiday_name = list.split(': ')
                datetime_ = datetime.datetime.strptime(day, '%Y-%m-%d')
                date = datetime_.date()
                holiday_dict[date] = holiday_name
            
            return holiday_dict
    
    def is_holiday(self, date):
        return date in self.holidays
    