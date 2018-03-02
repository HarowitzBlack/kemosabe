

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
class Kemosabe(configurations,Events):
    def __init__(self):
        pass

    # sets the configs and keeps them in a dict
    def set_configuration(self,read_from=""):
        print("reading conifg")
        configurations.set(self,path=read_from)

    # Use this class to set events
    def set_events(self,events):
        self.events = events
        Events.set_event_dict(self,self.events)

    # use this to run the bot
    def run(self,port):
        app.run(port=port)
