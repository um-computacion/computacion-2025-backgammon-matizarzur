from core.Dice import Dice
from unittest import TestCase
from unittest.mock import patch

#Para la creacion de los test se presenta el problema de que genera numeros aleatorios, entonces cada vez que ejecutamos el test obtendriamos resultados diferentes. Para esto se utiliza el mocking
#El mocking es remplazar temporalmente una funcion por una version controlada de la misma, asi podemos predecir los resultados.

class TestDice(TestCase):

    # @patch.object(Clase, 'metodo', side_effect=[5, 2])
    # def test_method(self, randint_patched):
    #     ...
    def setUp(self):
        self.dice = Dice()
        
    @patch('random.randint', side_effect=[5, 2])
    def test_simple(self, randint_patched):
        self.dice.roll()
        self.assertEqual(len(self.dice.last_roll), 2)
        self.assertEqual(self.dice.last_roll[0], 5)
        self.assertEqual(self.dice.last_roll[1], 2)
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
        with self.assertRaises(Exception):
            dice.roll()
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
        self.assertEqual(dice.get_moves_remaining(), 0)
        self.assertFalse(dice.is_double())

    def test_is_double_method(self):
        dice = Dice()
        with patch('random.randint', return_value=3):
            dice.roll()
            self.assertTrue(dice.is_double())
            dice.clear_roll()
            self.assertFalse(dice.is_double())
            
        with patch('random.randint', side_effect=[1, 6]):
            dice.roll()
            self.assertFalse(dice.is_double())
    
    def test_get_moves_remaining_method(self):
        self.assertEqual(Dice().get_moves_remaining(), 0)
        dice = Dice()
        with patch('random.randint', return_value=3):
            dice.roll()
            self.assertEqual(dice.get_moves_remaining(), 4)
            dice.clear_roll()
            self.assertEqual(dice.get_moves_remaining(), 0)
            self.assertFalse(dice.is_double())

    def test_clear_roll_method(self):
        dice = Dice()
        with patch('random.randint', return_value=3):
            dice.roll()
            self.assertEqual(dice.get_moves_remaining(), 4)
            dice.clear_roll()
            self.assertEqual(dice.get_moves_remaining(), 0)

    def test_last_roll_setter_valid_y_invalid(self):
        self.dice.last_roll= (3,4)
        self.assertEqual(self.dice.last_roll, (3,4))
        with self.assertRaises(ValueError):
            self.dice.last_roll = [3,4]
            
    def test_get_roll_values_none(self):
        self.assertIsNone(self.dice.get_roll_values())

    def test_get_roll_values_double(self):
        self.dice.last_roll = (5, 5, 5, 5)
        self.assertEqual(self.dice.get_roll_values(), (5, 5))

    def test_get_roll_values_normal(self):
        self.dice.last_roll = (2, 6)
        self.assertEqual(self.dice.get_roll_values(), (2, 6))

    def test_use_move_not_found(self):
        self.dice.last_roll = (2, 3)
        result = self.dice.use_move(5)  # no existe
        self.assertFalse(result)
        self.assertEqual(self.dice.last_roll, (2, 3))
        
    def test_use_move_not_found_branch(self):
        dice = Dice()
        dice.last_roll = (2, 3)
        result = dice.use_move(6)  # 6 no está en la tirada
        self.assertFalse(result)
        self.assertEqual(dice.last_roll, (2, 3))  # no cambia