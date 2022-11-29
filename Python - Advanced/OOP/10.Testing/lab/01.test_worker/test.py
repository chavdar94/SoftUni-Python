from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('TestName', 1000, 100)

    def test_correct_initialization(self):
        self.assertEqual('TestName', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_working_with_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increase_when_working(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_energy_decrease_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_rest_energy_increase(self):
        self.worker.energy = 0
        self.worker.rest()
        self.assertEqual(1, self.worker.energy)

    def test_get_info_return_message(self):
        self.assertEqual('TestName has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
