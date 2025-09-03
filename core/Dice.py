import random

class Dice:
    def __init__(self):
        self.last_roll = None
    
    def roll(self):
        try:
            dice_0 = random.randint(1, 6)
            dice_1 = random.randint(1, 6)
            
            if dice_0 == dice_1:
                self.last_roll = (dice_0, dice_1, dice_0, dice_1)
            else:
                self.last_roll = (dice_0, dice_1)
            
            return self.last_roll
        except Exception:
            return ()
    
    def is_double(self):
        if self.last_roll and len(self.last_roll) == 4:
            return True
        return False
    
    def get_moves_remaining(self):
        return len(self.last_roll) if self.last_roll else 0