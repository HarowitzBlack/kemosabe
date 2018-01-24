

class EntityRecorder():

    """ Keeps track of all the entities that come in with every request
        so that it can be accessed easily.

        ex: { 'id':1235,'msg':'Hey!','payload':'@start'}

        - add new entity to the dict using a method
        - show the entity dict

    """
    def __init__(self):
        self.__keeper = {}

    def add_entity(self,name,value):
        self.value = value
        self.name  = name
        self.__keeper[self.name] = self.value

    def get_entities(self):
        return self.__keeper

class Handler():

    def __init__(self,json_response):
        # json response is the data sent by facebook
        self.json_response = json_response
        self.entity_recorder = EntityRecorder()
        self.json_parser(self.json_response)
        print(self.entity_recorder.get_entities())

    def json_parser(self,json_data):
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
                            self.entity_recorder.add_entity("action",self.quick_payload)

                        if messages['message'].get('attachments'):
                            self.user_location = extract_user_location(messages)
                            self.entity_recorder.add_entity("location",self.user_location)




    def extract_quick_reply_payload(self,payload):
        if payload['message'].get('quick_reply'):
            return payload['message']['quick_reply']['payload']

    def extract_user_location(self,payload):
        if payload['message'].get('attachments'):
            if payload['message']['attachments'][0].get('payload'):
                if payload['message']['attachments'][0]['payload'].get('coordinates'):
                    return payload['message']['attachments'][0]['payload']['coordinates']




if __name__ == "__main__":
    pass
