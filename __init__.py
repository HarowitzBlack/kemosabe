

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
    def run(self,port,debug=False,threaded=False,set_menu=None):
        # send 'get_started' button request and run the bot
        # since everything will be loaded, no exception will be raised
        from .api import get_started_btn,send_menu
        from .helpers import simple_menu
        get_started_btn()
        if set_menu is None:
            # use the in-built menu
            # only triggers the @get_started()
            send_menu(simple_menu)
        else:
            send_menu(set_menu)

        app.run(port=port,debug=debug,threaded=threaded)
