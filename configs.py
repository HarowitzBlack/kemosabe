
print("configs module loaded")

class configurations():

    _configs = {}

    def __init__(self):
        #print("configs Loaded")
        pass

    def set(self,api_key=None,verify_token=None):
        if api_key == None:
            print("Set an api key")
        elif len(api_key) < 177:
            print("Invalid api key")

        if verify_token == None:
            print("Set a verification token")

        configurations._configs['api_token'] = api_key
        configurations._configs['vf_token']  = verify_token

    def get(self):
        print(configurations._configs)
        return configurations._configs
