from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_init(self):
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, }, self.store.toy_shelf)

    def test_add_toy_no_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('H', 'ToyName')
        err_msg = "Shelf doesn't exist!"
        self.assertEqual(err_msg, str(ex.exception))

    def test_add_toy_with_existing_toy_raises_exception(self):
        self.store.toy_shelf['A'] = 'Test Toy'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Test Toy')
        err_msg = 'Toy is already in shelf!'
        self.assertEqual(err_msg, str(ex.exception))

    def test_add_toy_shelf_is_not_none_raises_exception(self):
        self.store.toy_shelf['A'] = 'Test Toy'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'Test Shelf')
        err_msg = 'Shelf is already taken!'
        self.assertEqual(err_msg, str(ex.exception))

    def test_add_toy_expect_success(self):
        result = self.store.add_toy('A', 'Test Toy')
        self.assertEqual('Test Toy', self.store.toy_shelf['A'])
        msg = 'Toy:Test Toy placed successfully!'
        self.assertEqual(msg, result)

    def test_remove_toy_from_not_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('H', 'Test Toy')
        err_msg = "Shelf doesn't exist!"
        self.assertEqual(err_msg, str(ex.exception))

    def test_remove_toy_not_existing_toy_in_shelf(self):
        self.store.toy_shelf['A'] = 'Test Toy'
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'Test Toy2')
        err_msg = "Toy in that shelf doesn't exists!"
        self.assertEqual(err_msg, str(ex.exception))

    def test_remove_toy_expect_success(self):
        self.store.toy_shelf['A'] = 'Test Toy'
        result = self.store.remove_toy('A', 'Test Toy')
        self.assertEqual(self.store.toy_shelf['A'], None)
        msg = 'Remove toy:Test Toy successfully!'
        self.assertEqual(msg, result)
        

if __name__ == '__main__':
    main()
