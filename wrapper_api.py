

from .api import MessengerAPI
from .payload_builder import payload


token = "EAAExpe5DqoQBAILgztplgZBXj5IQrEj4wVpdItfR1LWGVZBC2MfJykoUPF25G92U4szjI96G1Gw6NfnrltgnQT2ShyW5PQgWZAKBYUHY6GlJ5OemZBbifLtMIVn1rObjNHs8IRpbEuXfZAXko5Rp6pg8GXbID1pN8n9TaZCkUo4AZDZD"
bot = MessengerAPI(token)
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
