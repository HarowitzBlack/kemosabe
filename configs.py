
import json
import os

class configurations():

    _configs = {}

    def __init__(self):
        self.fpath = ""
        print("loading...")

    def set(self,path):
        # reads from the json file and stores the configs in memory
        data = self.read_cfg_file(path=path)
        self.fpath = path
        configurations._configs['api_token'] = data["api_key"]
        configurations._configs['vf_token']  = data["verify_key"]

    def get(self):
        # allows access to the private configs
        data = self.read_cfg_file(path=self.fpath)
        return {"api_key":data["api_key"],"verify_key":data["verify_key"]}

    def read_cfg_file(self,path):
        if not path.endswith(".json"):
            # raise an exception
            print("configs must be a json file")
        print(path)
        npath = os.path.abspath(path)
        print(npath+path)
        with open("{}".format(path),"r") as cfg:
            data = cfg.read()
            data = json.loads(data)
            # raise an exception if the json properties are not found
            # or aren't set to the correct property names
            if not data.get("api_key") or not data.get("verify_key"):
                print("Couldn't find api key/verify key in '{0}'. Make sure you've set the \
                property names correctly(property names must be 'api_key'\
                and 'verify_key').".format(path))
        return data
