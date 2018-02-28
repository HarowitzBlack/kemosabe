

class configurations():

    _configs = {}

    def set(self,api_key=None,verify_token=None):
        if api_key == None:
            print("Set an api key")
        elif len(api_token) < 177:
            print("Invalid api key")

        if verify_token == None:
            print("Set a verification token")

        configurations._configs['api_token'] = api_key
        configurations._configs['vf_token']  = v_tok

    def get(self):
        return configurations._configs
