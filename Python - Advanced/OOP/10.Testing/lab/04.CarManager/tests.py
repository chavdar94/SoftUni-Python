from unittest import TestCase, main
# from car_manager import Car


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'Avensis', 4.9, 60)

    def test_correct_initialization(self):
        self.assertEqual('Toyota', self.car.make)
        self.assertEqual('Avensis', self.car.model)
        self.assertEqual(4.9, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_negative_or_zero_fuel_consumption_on_init_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_negative_or_zero_fuel_capacity_on_init_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount_less_than_zero_on_init_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel_with_zero_or_negative_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount_bigger_than_fuel_capacity(self):
        self.car.refuel(70)
        self.assertEqual(60, self.car.fuel_capacity)

    def test_refuel_adds_fuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_if_not_enough_fuel_raises_exception(self):
        self.car.fuel_amount = 20
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_valid_distance_expect_fuel_amount_decrease(self):
        self.car.fuel_amount = 60
        self.car.drive(100)

        self.assertEqual(55.1, self.car.fuel_amount)


if __name__ == '__main__':
    main()
