
import json

class configurations():

    _configs = {}

    def __init__(self):
        print("loading...")

    def set(self,path):
        data = self.read_cfg_file(path=path)
        configurations._configs['api_token'] = data["api_key"]
        configurations._configs['vf_token']  = data["verify_key"]

    def get(self):
        return configurations._configs

    def read_cfg_file(self,path):
        if not path.endswith(".json"):
            # raise an exception
            print("configs must be a json file")
        with open("{}".format(path),"r") as cfg:
            data = cfg.read()
            data = json.loads(data)
        return data
