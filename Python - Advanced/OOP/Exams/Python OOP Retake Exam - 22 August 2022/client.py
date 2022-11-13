class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.orders = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.startswith('0') and len(value) == 10 and value.isdigit():
            self.__phone_number = value
        else:
            raise ValueError('Invalid phone number!')
