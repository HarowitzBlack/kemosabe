

class Configurations():

    def __init__(self):
        self.keys = dict()

    def add(self,access_token=None,verify_token=None,**kwargs):
        if access_token == None:
            # raise an exception here
            # confignotfound!
            print("Need access token")
        if verify_token == None:
            # here too
            print("Need verify token")
        self.keys['access_token'] = access_token
        self.keys['verify_token'] = verify_token
        for kw,v in kwargs.items():
            self.keys[kw] = v

    def get(self):
        return self.keys

if __name__ == "__main__":
    x = Configurations()
    x.add(access_token="okfmv",verify_token="oklol")
    x.show()
