import random


class BaseEntity:

    def __init__(self, entity_type=-1):
        self.id = random.getrandbits(32)
        self.entity_type = entity_type
        self.current_state = None
        self.previous_state = None
        self.global_state = None

    def update(self):
        raise NotImplementedError

    def handle_message(self, telegram):
        raise NotImplementedError

    def revert_to_previous_state(self):
        raise NotImplementedError
