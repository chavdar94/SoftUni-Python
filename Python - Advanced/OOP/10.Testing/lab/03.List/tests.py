from unittest import TestCase, main


# from extended_list import IntegerList


class IntegerListsTests(TestCase):
    def setUp(self):
        self.list = IntegerList("1", 1, "a", 3.14, 2, 3)

    def test_correct_initialization(self):
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_corretct_get_data(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_list_add_if_el_not_int_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("1")

        self.assertTrue("Element is not Integer", str(ve.exception))

    def test_correct_add_integer_to_list(self):
        result = self.list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_remove_index_if_not_valid_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index(self):
        result = self.list.remove_index(2)

        self.assertNotIn(3, self.list._IntegerList__data)
        self.assertEqual(result, 3)

    def test_get_index_if_invalid_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_index_with_valid_index(self):
        result = self.list.get(2)
        self.assertEqual(result, 3)

    def test_insert_if_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(3, 4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_if_element_is_not_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(2, "4")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_params(self):
        self.list.insert(2, 4)

        self.assertEqual([1, 2, 4, 3], self.list._IntegerList__data)

    def test_get_biggest_returns_biggest_number(self):
        result = self.list.get_biggest()
        self.assertEqual(result, 3)

    def test_get_index(self):
        result = self.list.get_index(1)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    main()
