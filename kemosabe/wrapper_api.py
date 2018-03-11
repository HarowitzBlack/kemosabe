
from .configs import configurations
from .api import MessengerAPI
from .payload_builder import payload
from .exceptions import KeysNotFound,InternalError
import os,json

cfgs = configurations()
pload = payload()
bot = MessengerAPI()

def load_messenger_api():
    # call the class
    bot = MessengerAPI()

def send_text_message(uid,text):
    """Sends a text message to the user
    """
    r = bot.send_text_message(uid,text)
    return r

def send_quick_reply(uid,text,payload):
    """Sends quick reply to the user
    """
    r = bot.quick_reply(uid,text,payload)
    return r

def send_card_templates(uid,payload):
    """Constructs JSON response from a dict 
    """
    r = bot.generic_template(uid,payload)
    return r

def send_card_templates_raw(uid,raw_payload):
    """ Sends raw json template
    """
    r = bot.generic_template_raw(uid,raw_payload)
    return r

def create_action(action='',**kwargs):
    """ Builds the payload using the action and user-defined variables

    >> create_action(action="getallpetstores",pet="cat",color='white')

    result:
    >> @getallpetstores?&color=white&pet=cat

    """
    pstr = pload.create(action,**kwargs)
    return pstr

def parse(action='',**kwargs):
    """
    parses the payload string to extract params
    Used internally.
        >> @getallpetstores?&color=white&pet=cat

        result:
        >> {'color': 'white', 'pet': 'cat', 'action': '@getallpetstores'}
    """
    pstr = pload.parse(action,**kwargs)
    return pstr

def set_configurations(api_key=None,verify_key=None):
    # set the configs here
    if api_key == None and verify_key== None:
        raise KeysNotFound("Please set the keys in config.json file.")
    else:
        # pack it up and put it in a json file
        config_data = {"api_key":api_key,"verify_key":verify_key}
        try:
            with open("configs.json","w") as cfg_json:
                config_data = json.dumps(config_data)
                cfg_json.write(config_data)
        except Exception as e:
            raise InternalError("Could not create config.json file.Error:"+ e)
        else:
            # load the messenger api class if a config
            # file was created succesfully
            load_messenger_api()
