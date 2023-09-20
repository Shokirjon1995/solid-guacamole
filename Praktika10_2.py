class Player:
    def __init__(self, stamina, power, accuracy, speed):
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy
        self.speed = speed


class Attacker(Player):
    def __init__(self, power, speed, accuracy, goal):
        super().__init__(power, speed, accuracy)
        self.goal = goal

class defender(Player):
    def __init__(self, power, speed, stamina, tackling_the_ball):
        super().__init__(power, speed, stamina)
        self.tackling_the_ball = tackling_the_ball

class Goalkeeper(Player):
    def __init__(self, power, speed, dont_miss_the_ball):
        super().__init__(power, speed)
        self.dont_miss_the_ball = dont_miss_the_ball

class Midfielder(Player):
    def __init__(self, power, stamina, assist):
        super().__init__(power, stamina)
        self.assist = assist