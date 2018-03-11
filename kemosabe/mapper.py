
# INTERNAL LOGIC (o_o)



class DictoObj(object):
    """ Convert the ugly dict into an object
    """

    def __init__(self,d):
        self.__dict__.update(d)

class Mapper():

    """ This class is the core part of Kemosabe.
        All you need to know is this class triggers
        the function that's mapped to it's corresponding
        action.

        ex:
            {"@someaction": some_function_to_trigger,} ==> some_function_to_trigger()

    """

    def __init__(self, session_dict, actions):
        self.session_dict = session_dict
        # convert the dict to a python object
        self.session_attr = DictoObj(self.session_dict)
        self.actions = actions
        if self.session_dict:
            # event is triggered if the action tag is
            # found in the dict.
            if self.session_dict.get("action"):
                self.user_action = self.session_dict["action"]
                self.trigger_action()

            # fall back event is triggered only if text is present in the dict
            # Due to the nature of buttons/quick reply buttons, they send
            # the display text as a text property in the response. The extractor
            # extracts the text property thinking it is the text sent by the user.
            # So, hopefully this fixes the problem.
            if self.session_dict.get("text"):
                # trigger the event only if the text is sent by the user.
                # To determine what is sent by the user, we check if
                # the dict contains an action key. If it does we know that
                # the action event happens only if the user taps on a component.
                if not self.session_dict.get("action"):
                    # set to a default event. Must be mapped in the event dict.
                    self.user_action = "@text"
                    self.trigger_action()


    def trigger_action(self):
        # triggers the function
        for dict_key in self.actions.keys():
            if dict_key == self.user_action:
                # verify whether this request is the actual response sent by FB
                # FB sends 2 responses, one with the content and the other without it
                # If the session_dict has more than 1 item, then it is the
                # response we are looking for.
                if len(self.session_dict) > 1:
                    self.actions[dict_key](self.session_attr)
                    print("session attributes:",vars(self.session_attr))
                else:
                    pass
