

from .api import MessengerAPI
from .api import *

token = ""

bot = MessengerAPI(token)

def send_text_message(uid,text):
    r = bot.send_text_message(uid,text)
    return r

def send_quick_reply(uid,text,payload):
    r = bot.quick_reply(uid,text,payload)
    return r
