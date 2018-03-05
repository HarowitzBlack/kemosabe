

from .exceptions import EventNotFoundError
# event class should load the event dict and check for the correct format
class Events():

    e_dict = {}

    def set_event_dict(self,event_dict):
        Events.e_dict = event_dict
        self.load_events()


    def check_event_dict(self,event_dict):
        if len(event_dict) == 0:
            raise EventNotFoundError("Event dict cannot be empty.")

        # check for event format
        if "@get_started" not in event_dict.keys():
            raise EventNotFoundError("Event dict must have @get_started event.")

        for e in event_dict.keys():
            if not e.startswith("@"):
                raise EventNotFoundError("Event '{0}' must start with '@'".format(e))
        return event_dict

    def load_events(self):
        edict = self.check_event_dict(Events.e_dict)
        return edict
