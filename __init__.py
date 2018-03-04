

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
import json



# app class
class Kemosabe(configurations,Events):
    def __init__(self):
        pass

    # sets the configs and keeps them in a dict
    def set_keys(self,api_key=None,verify_key=None):
        # call the set_configurations() from wrapper api
        # This is just a high level wrapper.
        set_configurations(api_key=api_key,verify_key=verify_key)


    # Use this class to set events
    def set_events(self,events):
        self.events = events
        Events.set_event_dict(self,self.events)

    # use this to run the bot
    def run(self,port,debug=False,threaded=False):
        app.run(port=port,debug=debug,threaded=threaded)
