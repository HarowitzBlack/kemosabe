

"""
Kemosabe
copyright 2018 (C)
"""


__author__      = 'Joel Benjamin (HarowitzBlack)'
__version__     = '0.9.0'


from .configs import configurations
from .wrapper_api import *
from .events import Events
from .app import Application

# top level interface layer
class Kemosabe(configurations,Events):
    def __init__(self,events):
        self.main_events = events
        self.app = Application()

    # sets the configs and keeps them in a dict
    def set_keys(self,api_key=None,verify_key=None):
        """ Interface to set configs in the config class
        """
        # calling the set_configurations() from wrapper api
        # This is just a high level wrapper.
        set_configurations(api_key=api_key,verify_key=verify_key)
        self.set_events()

    def set_events(self):
        """ Interface to set events in the event class
        """
        self.events = self.main_events
        Events.set_event_dict(self,self.events)

    def run(self,host_name='127.0.0.1',port=5000,set_menu=None,enable_text=True):
        self.app.run(host=host_name,port=port,set_menu=set_menu,enable_text=enable_text)
