from base_entity import BaseEntity
from state import WifeGlobalState


class Wife(BaseEntity):
    def __init__(self, current_state=None, location=None):
        super().__init__()
        self.current_state = current_state
        self.previous_state = None
        self.global_state = WifeGlobalState()
        self.location = location
        self.is_cooking = False
        self.stress_level = 0

        self.other_entity = None

        self.STRESS_THRESHOLD = 3

    def update(self):
        self.stress_level += 1
        if self.current_state:
            self.current_state.execute(self)

    def handle_message(self, telegram):
        self.global_state.on_message(self, telegram)
        self.current_state.on_message(self, telegram)

    def change_state(self, new_state):
        if not self.current_state and not new_state:
            return

        self.current_state.exit(self)

        self.current_state = new_state

        self.current_state.enter(self)

    def revert_to_previous_state(self):
        self.current_state = self.previous_state

    def set_is_cooking(self, is_cooking):
        self.is_cooking = is_cooking

    def is_stressed(self):
        return self.stress_level >= self.STRESS_THRESHOLD
