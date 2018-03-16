

"""
Kemosabe - A bot framework to build bots with less code.

MIT License

Copyright (c) 2018 Joel Benjamin(HarowitzBlack)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""


__author__      = 'Joel Benjamin (HarowitzBlack)'
__version__     = '0.8.2'


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
