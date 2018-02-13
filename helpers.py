
import os
import json

def get_token():
    try:
        with open("./configs.json","r") as cf:
            key_dta = cf.read()
            key_dta = json.loads(key_dta)
            return key_dta['api_token']
    except FileNotFoundError:
        # raise an exception
        print("File not found.Try setting the configs using the set_configurations method")
