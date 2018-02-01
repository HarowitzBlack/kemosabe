
import actionMapper
import payload_parser



class EntityRecorder():

    """ Keeps track of all the entities that come in with every request.

        ex: { 'id':1235,'msg':'Hey!','payload':'@start'}

        * add new entity to the dict using a method
        * show the entity dict

    """
    def __init__(self):
        self.__keeper = {}

    def add_entity(self,name,value):
        """ Insert the value into the dict """
        self.value = value
        self.name  = name
        self.__keeper[self.name] = self.value

    def get_entities(self):
        """ return the dict """
        return self.__keeper

class Handler():
    """This class extracts the required data from the json response sent by fb for every request.
       After extracting the data, it sends it over to the ActionMapper Class. The mapped action is
       called from the ActionMapper Class and whoohooo! The bot responds!!

       json_parser extracts: text,location, quick replies actions and button click actions

       #TODO : extract images,videos and audio files

    """

    def __init__(self,json_response,actions):
        # json response is the data sent by facebook
        self.json_response = json_response
        self.actions = actions
        self.entity_recorder = EntityRecorder()
        self.payload_extractor = payload_parser.builder()
        self.json_parser(self.json_response)
        # handler should call the mapper class
        # json_parser method strips down the json data and inserts
        # them into the entity_recorder object
        # It can be accessed by using the get_entities() method of
        # the EntityRecorder Class
        self.entities = self.entity_recorder.get_entities()
        actionMapper.Mapper(self.entities,self.actions)


    def json_parser(self,json_data):
        """ Extracts data from json_data and inserts them into the entity_recorder
            Object, which will make all the data available for the next request.

        """
        self.json_data = json_data['entry']
        for entry in self.json_data:
            if entry.get("messaging"):
                for messages in entry['messaging']:
                    self.user_id = messages['sender']['id']
                    self.entity_recorder.add_entity("id",self.user_id)
                    if messages.get('message'):
                        if messages['message'].get('text'):
                            self.text_msg = messages['message']['text']
                            self.entity_recorder.add_entity("text",self.text_msg)
                        if messages['message'].get('quick_reply'):
                            self.quick_payload = self.extract_quick_reply_payload(messages)
                            p_load = self.payload_extractor.parse_payload(self.quick_payload)
                            print(p_load)
                            for pk,v in p_load.items():
                                self.entity_recorder.add_entity(pk,v)
                            

                        if messages['message'].get('attachments'):
                            self.user_location = self.extract_user_location(messages)
                            self.entity_recorder.add_entity("location",self.user_location)

                    if messages.get('postback'):  # for postback getstarted button
                        self.user_action = self.extract_user_payload(messages)
                        self.entity_recorder.add_entity("action",self.user_action)

    def extract_quick_reply_payload(self,payload):
        """ Extract action from quick reply """
        if payload['message'].get('quick_reply'):
            return payload['message']['quick_reply']['payload']

    def extract_user_location(self,payload):
        """ Extract coordinates dict """
        if payload['message'].get('attachments'):
            if payload['message']['attachments'][0].get('payload'):
                if payload['message']['attachments'][0]['payload'].get('coordinates'):
                    return payload['message']['attachments'][0]['payload']['coordinates']

    def extract_user_payload(self,payload):
        """ Extract action from the postback response """
        if payload.get('postback'):  # for postback getstarted button
            if payload['postback'].get('referral'):
                if payload['postback']['referral'].get('ref'):
                    return payload['postback']['referral']['ref']
            if payload['postback'].get('payload'):
                return payload['postback']['payload']




if __name__ == "__main__":
    pass
