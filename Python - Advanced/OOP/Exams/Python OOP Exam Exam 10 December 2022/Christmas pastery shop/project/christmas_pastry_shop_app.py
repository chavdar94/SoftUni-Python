from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    valid_delicacies = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }

    valid_booths = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.valid_delicacies:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

        if name in [d.name for d in self.delicacies]:
            raise Exception(f'{name} already exists!')

        delicacy = self.valid_delicacies[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if type_booth not in self.valid_booths:
            raise Exception(f'{type_booth} is not a valid booth!')

        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f'Booth number {booth_number} already exists!')

        booth = self.valid_booths[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        booths = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved]
        if not booths:
            raise Exception(f'No available booth for {number_of_people} people!')

        booth = booths[0]
        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in [b.booth_number for b in self.booths]:
            raise Exception(f'Could not find booth {booth_number}!')

        if delicacy_name not in [d.name for d in self.delicacies]:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]

        current_income = booth.price_for_reservation
        for order in booth.delicacy_orders:
            current_income += order.price

        self.income += current_income
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        result = [
            f'Booth {booth.booth_number}:',
            f'Bill: {current_income:.2f}lv.'
        ]

        return '\n'.join(result)

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'

