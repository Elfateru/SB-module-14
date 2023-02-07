class Date:

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {} Месяц: {} Год: {}'.format(
            self.day, self.month, self.year
        )

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        print(date_obj)
        return date_obj

    @staticmethod
    def is_date_valid(date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        if month == 2:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return 0 < day <= 29 and year > 0
            else:
                return 0 < day <= 28 and year > 0
        else:
            if 0 < month <= 7:
                if month % 2 == 1:
                    return 0 < day <= 31 and year > 0
            elif 7 < month <= 12:
                if month % 2 == 0:
                    return 0 < day <= 31 and year > 0
            else:
                return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('29-2-2005'))
print(Date.is_date_valid('29-2-2004'))
