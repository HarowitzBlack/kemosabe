

# NOT USED YET. FOR FUTURE USE PERHAPS?

class Configurations():

    def __init__(self):
        print("Yeah configs loaded")
        self.keys = {"access_token":"","verify_token":""}

    def set(self,access_token=None,verify_token=None,**kwargs):
        """ sets the config keys. You'll know the rest.
        """
        if access_token == None or verify_token == None:
            print("Need access token")
        # put the configs in the dict
        self.keys['access_token'] = access_token
        self.keys['verify_token'] = verify_token
        # puts additional configs in the dict
        for kw,v in kwargs.items():
            self.keys[kw] = v

    def get(self):
        return self.keys

if __name__ == "__main__":
    x = Configurations()
    x.set(access_token="okfmv",verify_token="oklol")
    x.get()
