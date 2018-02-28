

"""
Kemosabe
copyright 2018 (c)

"""


__author__      = 'Joel Benjamin (HarowitzBlack)'
__version__     = '0.9.0'


from .configs import configurations
from .events import Events
from .run import app
from .wrapper_api import *


# app class
class Kemosabe():
    def __init__(self):
        event = Events()

    # sets the configs and keeps them in a dict
    def set_configuration(self,api_key=None,verify_token=None):
        # func in wrapper_api module
        set_configurations(api_key=api_key,verify_token=verify_token)

    # Use this class to set events
    def set_events(self,events):
        self.events = events
        event.set_event_dict(self.events)

    # use this to run the bot
    def run(port=8080):
        app.run(port=port)
