months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
status = {
    True: 'rented',
    False: 'not rented'
}


class DVD:

    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split('.')]

        return cls(name, id_number, year, months[month], age_restriction)

    def __repr__(self):
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) ' \
               f'has age restriction {self.age_restriction}. Status: {status[self.is_rented]}'
