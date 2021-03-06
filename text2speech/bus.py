from jarbas_utils.messagebus import Message


class FakeBus:
    events = {}
    once_events = {}

    def __init__(self, *args, **kwargs):
        pass

    def on(self, msg_type, handler):
        if msg_type not in self.events:
            self.events[msg_type] = []
        self.events[msg_type].append(handler)

    def once(self, msg_type, handler):
        if msg_type not in self.once_events:
            self.once_events[msg_type] = []
        self.once_events[msg_type].append(handler)

    def emit(self, message):
        if message.msg_type in self.events:
            for handler in self.events[message.msg_type]:
                handler(message)
        if message.msg_type in self.once_events:
            for handler in self.once_events[message.msg_type]:
                handler(message)
            self.once_events.pop(message.msg_type)

    def remove(self, msg_type, handler):
        pass


bus = FakeBus()
