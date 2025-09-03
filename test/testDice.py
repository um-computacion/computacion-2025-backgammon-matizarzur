from core.Dice import Dice
from unittest import TestCase
from unittest.mock import patch

#Para la creacion de los test se presenta el problema de que genera numeros aleatorios, entonces cada vez que ejecutamos el test obtendriamos resultados diferentes. Para esto se utiliza el mocking
#El mocking es remplazar temporalmente una funcion por una version controlada de la misma, asi podemos predecir los resultados.

class TestDice(TestCase):

    # @patch.object(Clase, 'metodo', side_effect=[5, 2])
    # def test_method(self, randint_patched):
    #     ...

    @patch('random.randint', side_effect=[5, 2])
    def test_simple(self, randint_patched):
        dice = Dice()
        dice.roll()
        self.assertEqual(len(dice.last_roll), 2)
        self.assertEqual(dice.last_roll[0], 5)
        self.assertEqual(dice.last_roll[1], 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', return_value=1)
    def test_complex(self, randint_patched):
        dice = Dice()
        dice.roll()
        self.assertEqual(len(dice.last_roll), 4)
        self.assertEqual(dice.last_roll[0], 1)
        self.assertEqual(dice.last_roll[1], 1)
        self.assertEqual(dice.last_roll[2], 1)
        self.assertEqual(dice.last_roll[3], 1)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', side_effect=Exception("error!!"))
    def test_error(self, randint_patched):
        dice = Dice()
        dice.roll()
        self.assertEqual(len(dice.last_roll), 0)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 1)


    def test_double(self):
        with patch('random.randint', side_effect=[5, 2]) as randint_patched:
            dice = Dice()
            dice.roll()
            self.assertEqual(len(dice.last_roll), 2)
            self.assertEqual(dice.last_roll[0], 5)
            self.assertEqual(dice.last_roll[1], 2)
            self.assertTrue(randint_patched.called)
            self.assertEqual(randint_patched.call_count, 2)

        with patch('random.randint', return_value=1) as randint_patched:
            dice = Dice()
            dice.roll()
            self.assertEqual(len(dice.last_roll), 4)
            self.assertEqual(dice.last_roll[0], 1)
            self.assertEqual(dice.last_roll[1], 1)
            self.assertEqual(dice.last_roll[2], 1)
            self.assertEqual(dice.last_roll[3], 1)
            self.assertTrue(randint_patched.called)
            self.assertEqual(randint_patched.call_count, 2)

    def test_dice_initial_state(self):
        dice = Dice()
        self.assertIsNone(dice.last_roll)

    def test_is_double_method(self):
        dice = Dice()
        with patch('random.randint', return_value=3):
            dice.roll()
            self.assertTrue(dice.is_double())
            
        with patch('random.randint', side_effect=[1, 6]):
            dice.roll()
            self.assertFalse(dice.is_double())