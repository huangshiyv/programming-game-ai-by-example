from west_world.base_entity import BaseEntity


class Miner(BaseEntity):

    def __init__(self, current_state=None, location=None):
        super().__init__()
        self.current_state = current_state
        self.location = location
        self.wealth = 0
        self.gold_carried = 0
        self.money_in_the_bank = 0
        self.thirst = 0
        self.fatigue = 0

        self.COMFORT_LEVEL = 5
        self.MAX_NUGGETS = 3
        self.THIRST_LEVEL = 5
        self.TIREDNESS_THRESHOLD = 5

    def update(self):
        self.thirst += 1
        if self.current_state:
            self.current_state.execute(self)

    def change_state(self, new_state):
        if not self.current_state and not new_state:
            return

        self.current_state.exit(self)

        self.current_state = new_state

        self.current_state.enter(self)

    def change_location(self, new_location):
        self.location = new_location

    def add_to_wealth(self, gold=0):
        self.wealth += gold

    # Gold
    def increase_gold_carried(self, gold=1):
        self.gold_carried += gold

    def set_gold_carried(self, gold=0):
        self.gold_carried = gold

    def pockets_full(self):
        return self.gold_carried >= self.MAX_NUGGETS

    # Thirst
    def increase_thirsty(self, thirst=1):
        self.thirst += thirst

    def is_thirsty(self):
        return self.thirst >= self.THIRST_LEVEL

    # Fatigue
    def increase_fatigue(self, fatigue=1):
        self.fatigue += fatigue

    def decrease_fatigue(self, fatigue=1):
        self.fatigue -= fatigue

    def is_fatigue(self):
        return self.fatigue >= self.TIREDNESS_THRESHOLD

    # Buy and Drink
    def buy_and_drink_whiskey(self):
        self.thirst = 0
        self.wealth -= 2
