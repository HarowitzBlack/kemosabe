

class builder():


    def create_payload(self,action='',**kwargs):
        """ Builds the payload when action and params are given

            >> create_payload(action="getallpetstores",pet="cat",color='white')

            result:
            >> @getallpetstores?&color=white&pet=cat

        """
        self.action = action
        self.final_str = ''
        if self.action == '':
            print("action can't be empty")
            return
        self.final_str = "@" + self.action + "?"
        for key,value in kwargs.items():
            self.final_str += "&{}={}".format(key,value)
        return self.final_str


    def parse_payload(self,string):
        """ parses the payload string to extract params
            >> @getallpetstores?&color=white&pet=cat

            result:
            >> {'color': 'white', 'pet': 'cat', 'action': '@getallpetstores'}
        """
        self.final_dict = {}
        self.string = string
        # split the str to extract action trigger and other args
        split_list = self.string.split('?')
        # action trigger
        action_trigger = split_list[0]
        self.final_dict['action'] = action_trigger

        #extracting the args
        params = split_list[1].split('&')
        for p in params:
            if p == '':
                pass
            else:
                args = p.split('=')
                key = args[0]
                value = args[1]
                self.final_dict[key] = value
        return self.final_dict
