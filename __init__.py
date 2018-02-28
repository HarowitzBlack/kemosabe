

"""
Kemosabe
copyright 2018 (c)

"""


__author__      = 'Joel Benjamin (HarowitzBlack)'
__version__     = '0.9.0'


from .wrapper_api import *
from .configs import Configurations
from .run import app

# run the app
app.run(port=5002)
