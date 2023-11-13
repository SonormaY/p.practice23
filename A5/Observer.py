from A5.Logger import Logger

class Observer:
    def __init__(self):
        self.events = {
            "add":Logger.printToFile,
            "delete":Logger.printToFile,
            "clear":Logger.printToFile,
            "read":Logger.printToFile

        }

    def add_event(self, event_type, callback):
        self.events[event_type] = callback

    def handle_event(self, event):
        if event.type in self.events:
            self.events[event.type](event.data[0], event.data[1])
        else:
            raise Exception("Unknown event type")

class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

    def trigger(self, observer):
        observer.handle_event(self)