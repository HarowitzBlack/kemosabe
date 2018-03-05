
# not used anywhere

import os
import json

simple_menu = {

    "persistent_menu":[
        {
          "locale":"default",
          "composer_input_disabled": True,
          "call_to_actions":[
            {
                "title":"Start Over",
                "type":"postback",
                "payload":"@get_started"
            }
          ]
        }
    ]
}

def get_token():
    try:
        with open("./configs.json","r") as cf:
            key_dta = cf.read()
            key_dta = json.loads(key_dta)
            return key_dta['api_token']
    except FileNotFoundError:
        print("Couldn't find the config file. Use the set_configurations(api_key= YOUR_KEY) method first")

def show_message(mtype='s',msg=""):
    """
    Use this function to show error,warning or success messages.

    """
    if mtype == "e":
        print("\n\nError:{}\n\n".format(msg))
    elif mtype == "w":
        print("\n\nWarning:{}\n\n".format(msg))
    elif mtype == "s":
        print("\n\nSucess:{}\n\n".format(msg))
