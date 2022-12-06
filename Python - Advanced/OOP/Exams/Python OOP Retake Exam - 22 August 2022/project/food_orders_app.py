from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 1

    def __check_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __get_menu(self):
        return {meal.name: meal for meal in self.menu}

    def __find_or_create_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return new_client

    @staticmethod
    def __meal_in_menu(meal_names_and_quantities, menu):
        for meal in meal_names_and_quantities:
            if meal not in menu:
                raise Exception(f"{meal} is not on the menu!")

    @staticmethod
    def __enough_quantity(meal_names_and_quantities, menu):
        for meal, quantity in meal_names_and_quantities.items():
            if menu[meal].quantity < quantity:
                raise Exception(
                    f"Not enough quantity of {menu[meal].__class__.__name__}: {meal}!")

    @staticmethod
    def __empty_cart(client_cart):
        if not client_cart:
            raise Exception('There are no ordered meals!')

    @staticmethod
    def __reset_data(client_info):
        client_info.bill = 0
        client_info.shopping_cart = []
        client_info.orders = {}

    def register_client(self, client_phone_number: str):
        for client_num in self.clients_list:
            if client_num.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ("Starter", "MainDish", "Dessert"):
                self.menu.append(meal)

    def show_menu(self):
        self.__check_menu()
        meals = [str(meal.details()) for meal in self.menu]

        return '\n'.join(meals)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities: dict):
        self.__check_menu()
        client = self.__find_or_create_client(client_phone_number)
        menu = self.__get_menu()
        self.__meal_in_menu(meal_names_and_quantities, menu)
        self.__enough_quantity(meal_names_and_quantities, menu)

        for name, quantity in meal_names_and_quantities.items():
            menu[name].quantity -= quantity
            client.shopping_cart.append(menu[name])

        client.bill += sum(menu[name].price * quantity for name, quantity in meal_names_and_quantities.items())
        client.orders.update(meal_names_and_quantities)

        return f'Client {client_phone_number} successfully ordered {", ".join(meal.name for meal in client.shopping_cart)}' \
               f' for {client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number: str):

        client = self.__find_or_create_client(client_phone_number)
        self.__empty_cart(client.shopping_cart)

        menu = self.__get_menu()
        for name, quantity in client.orders.items():
            for menu_meal in self.menu:
                if name == menu_meal.name:
                    menu_meal.quantity += quantity

        self.__reset_data(client)
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = self.__find_or_create_client(client_phone_number)
        self.__empty_cart(client.shopping_cart)
        current_receipt_id = self.receipt_id
        self.receipt_id += 1
        money_to_pay = client.bill
        self.__reset_data(client)

        return f'Receipt #{current_receipt_id} with total amount of {money_to_pay:.2f}' \
               f' was successfully paid for {client_phone_number}.'

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'

