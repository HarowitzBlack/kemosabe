

from .api import MessengerAPI
from .payload_builder import payload
from .configs import configurations
import os
import json


bot = MessengerAPI()
pload = payload()
cfgs = configurations()


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
    r = bot.generic_template(uid,payload)
    return r

def create(action='',**kwargs):
    """ Builds the payload using the action and user-defined variables

    >> create_payload(action="getallpetstores",pet="cat",color='white')

    result:
    >> @getallpetstores?&color=white&pet=cat

    """
    pstr = pload.create(action,**kwargs)
    return pstr

def parse(action='',**kwargs):
    """
    parses the payload string to extract params
        >> @getallpetstores?&color=white&pet=cat

        result:
        >> {'color': 'white', 'pet': 'cat', 'action': '@getallpetstores'}
    """
    pstr = pload.parse(action,**kwargs)
    return pstr

def set_configurations(api_key=None,verify_token=None):
    # set the configs here
    cfgs.set(api_key=api_key,verify_token=verify_token)
