

from .api import MessengerAPI
from .payload_builder import payload
import os
import json


bot = MessengerAPI()
pload = payload()


def send_text_message(uid,text):
    r = bot.send_text_message(uid,text)
    return r

def send_quick_reply(uid,text,payload):
    r = bot.quick_reply(uid,text,payload)
    return r

def send_card_templates(uid,payload):
    r = bot.generic_template(uid,payload)
    return r

def create(action='',**kwargs):
    pstr = pload.create(action,**kwargs)
    return pstr

def parse(action='',**kwargs):
    pstr = pload.parse(action,**kwargs)
    return pstr

def set_configurations(api_key="",path="."):
    """
        
    """
    if api_key == "" or len(api_key) < 177:
        print("Invalid configs")
        return

    pth = path + "/configs.json"
    try:
        with open(pth,"w") as config_file:
            keys = {
                "api_token":api_key,
            }
            key_str = json.dumps(keys)
            config_file.write(key_str)
    except Exception as e:
        print(e)
