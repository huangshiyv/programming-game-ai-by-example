import random


class BaseEntity(object):

    def __init__(self, entity_type=-1):
        self.id = random.getrandbits(32)
        self.entity_type = entity_type
        self.current_state = None
        self.previous_state = None

    def update(self):
        raise NotImplementedError
