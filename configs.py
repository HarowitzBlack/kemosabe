
import json
import os

class configurations():

    _configs = {}

    def __init__(self):
        # If you're wondering why the code is messed up? You should know that
        # it's written by a 17 year old kid. Clearly, I know I have to learn a ton.
        pass

    def get(self):
        # allows access to the private configs
        data = self.read_cfg_file()
        return {"api_key":data["api_key"],"verify_key":data["verify_key"]}

    def read_cfg_file(self):
         # read the file and get the creds
         with open("configs.json","r") as cfg_data:
             creds = cfg_data.read()
             creds = json.loads(creds)
             return creds
