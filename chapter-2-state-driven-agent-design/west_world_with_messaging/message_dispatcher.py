import datetime

from telegram import Telegram
from message_types import message_type_to_string


class MessageDispatcher:

    def discharge(self, receiver, telegram):
        receiver.handle_message(telegram)

    def dispatch_message(self, delay, sender, receiver, message_type, extra_info):
        if receiver is None:
            print('No receiver')
            return

        telegram = Telegram(sender, receiver, message_type, datetime.datetime.now(), extra_info)

        if delay <= 0:
            print('Instant telegram dispatched at time: {} by {} for {} and message is: {}'.format(
                datetime.datetime.now(),
                sender.id,
                receiver.id,
                message_type_to_string(message_type)))

            self.discharge(receiver, telegram)
