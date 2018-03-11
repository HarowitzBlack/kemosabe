

from .payload_builder import payload
from .mapper import Mapper
from .helpers import show_message
import time
import hashlib


class session():

    """ Keeps track of all the entities that come in with every request.

        ex: { 'id':1235,'msg':'Hey!','payload':'@start'}
    """
    def __init__(self):
        self.__items_in_session = {}

    def add_to_session(self,name,value):
        """ Insert the value into the dict """
        self.value = value
        self.name  = name
        self.__items_in_session[self.name] = self.value

    def get_session_variables(self):
        """ return the dict """
        return self.__items_in_session

class Handler():
    """This class extracts the required data from the json response sent by fb for every request.
       After extracting the data, it sends it over to the ActionMapper Class. The mapped action is
       called from the ActionMapper Class and whoohooo! The bot responds!!

       json_parser extracts: text,location, quick replies actions and button click actions

       #TODO : extract images,videos and audio files

    """

    def __init__(self,json_response,actions):
        self.json_response = json_response
        self.actions = actions
        self.session = session()
        self.payload_extractor = payload()
        try:
            self.json_parser(self.json_response)
        except:
            show_message('e',"JSON error. Couldn't parse the data")
        # handler should call the mapper class
        # json_parser method strips down the json data and inserts
        # them into the session object
        # It can be accessed by using the get_session_variables() method of
        # the session Class
        self.session_variables = self.session.get_session_variables()
        Mapper(self.session_variables,self.actions)

    def json_parser(self,json_data):
        """ Extracts data from json_data and inserts them into the entity_recorder
            Object, which will make all the data available for the next request.

        """
        self.json_data = json_data['entry']
        for entry in self.json_data:
            if entry.get("messaging"):
                for messages in entry['messaging']:
                    self.user_id = messages['sender']['id']
                    self.session.add_to_session("id",self.user_id)
                    # add a unique id to every msg
                    hash_msg = "63cade1d33722aef702281225ca15c03229aabd8"
                    new_hash_msg = hash_msg + str(round(time.time()))
                    msg = hashlib.md5(new_hash_msg.encode()).hexdigest()
                    self.session.add_to_session("unique_id",msg)
                    if messages.get('message'):
                        if messages['message'].get('text'):
                            self.text_msg = messages['message']['text']
                            self.session.add_to_session("text",self.text_msg)
                        if messages['message'].get('quick_reply'):
                            self.quick_payload = self.extract_quick_reply_payload(messages)
                            p_load = self.payload_extractor.parse(self.quick_payload)
                            #print(p_load)
                            for pk,v in p_load.items():
                                self.session.add_to_session(pk,v)


                        if messages['message'].get('attachments'):
                            self.user_location = self.extract_user_location(messages)
                            self.session.add_to_session("location",self.user_location)

                    if messages.get('postback'):  # for postback getstarted button
                        self.user_action = self.extract_user_payload(messages)
                        self.session.add_to_session("action",self.user_action)

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
        # digging through the source code, huh? good luck, you'll find something ;)
        """ Extract action from the postback response """
        if payload.get('postback'):  # for postback getstarted button
            if payload['postback'].get('referral'):
                if payload['postback']['referral'].get('ref'):
                    return payload['postback']['referral']['ref']
            if payload['postback'].get('payload'):
                return payload['postback']['payload']


if __name__ == "__main__":
    pass
