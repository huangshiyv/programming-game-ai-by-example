from enum import Enum


class MessageTypes(Enum):
    HI_HONEY_I_AM_HOME = 1
    STEW_READY = 2


def message_type_to_string(message_type):
    if message_type == MessageTypes.HI_HONEY_I_AM_HOME:
        return 'Hi honey I am home'
    elif message_type == MessageTypes.STEW_READY:
        return 'Stew Ready'
    else:
        return 'Not recognised'
