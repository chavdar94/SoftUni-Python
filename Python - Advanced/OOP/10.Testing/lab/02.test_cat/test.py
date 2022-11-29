from unittest import TestCase, main
# from cat import Cat


class CatTests(TestCase):
    
    def setUp(self):
        self.cat = Cat('TestCat')
    
    def test_correct_initialization(self):
        self.assertEqual('TestCat', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
    
    def test_cat_valid_eat(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)
    
    def test_eat_raises_exception_if_already_fed(self):
        self.cat.fed = True
        
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        
        self.assertEqual('Already fed.', str(ex.exception))
    
    def test_cat_eat_set_fed_to_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
    
    def test_cat_eat_set_sleepy_to_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
    
    def test_cat_eat_increase_size_by_one(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
    
    def test_cat_sleep_if_not_fed_raises_exception(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleep_sets_sleepy_to_false(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy) 

if __name__ == '__main__':
    main()