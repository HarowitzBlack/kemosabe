
print("events module loaded")

# event class should load the event dict and check for the correct format
class Events():

    e_dict = {}

    def set_event_dict(self,event_dict):
        Events.e_dict = event_dict


    def check_event_dict(self,event_dict):
        # check for event format
        if "@get_started" not in event_dict.keys():
            # raise an exception
            print("event dict must have @get_started event.")

        for e in event_dict.keys():
            if not e.startswith("@"):
                print("event must start with '@'")

        return self.event_dict()

    def load_events():
        edict = self.check_event_dict(Events.e_dict)
        return edict
