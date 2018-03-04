
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
        self.session_attr = DictoObj(self.session_dict)
        self.actions = actions
        if self.session_dict:
            print(self.session_dict)
            #try:
                # raises error if the input is text
            print(self.session_dict)
            try:
                self.user_action = self.session_dict['action']
            except:
                self.user_action = "@fallback"
            self.trigger_action()
            #except Exception as e:
            #    print("error:",e)

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
