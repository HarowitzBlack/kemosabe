

class Configurations():

    def __init__(self):
        self.keys = {"access_token":"","verify_token":""}

    def set(self,access_token=None,verify_token=None,**kwargs):
        """ sets the config keys. You'll know the rest.
        """
        if access_token == None:
            # raise an exception here
            # confignotfound!
            print("Need access token")
        if verify_token == None:
            # here too
            print("Need verify token")
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
