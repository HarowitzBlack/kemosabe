
class Mapper():


    def __init__(self, entity_dict, actions):
        self.entity_dict = entity_dict
        self.actions = actions
        if self.entity_dict:
            try:
                print("mapper:",self.entity_dict)
                self.user_action = self.entity_dict['action']
                self.trigger_action()
            except:
                pass

    def trigger_action(self):
        for dict_key in self.actions.keys():
            if dict_key == self.user_action:
                # verify whether this request is the actual response sent by FB
                if len(self.entity_dict) > 1:
                    print("actions:",self.user_action)
                    self.actions[dict_key](self.entity_dict)
                else:
                    pass
