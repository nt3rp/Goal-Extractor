import httplib
from oauth.client import SimpleOAuthClient

class FortyTwoGoals(SimpleOAuthClient):
    def __init__(self):
        self.server = "http://api.42goals.com"
        self.port = 80
        self.request_token_url = "http://api.42goals.com/v1/oauth/request_token/"
        self.access_token_url = "http://api.42goals.com/v1/oauth/access_token/"
        self.authorization_url = " http://42goals.com/settings/authorize/$REQUEST_TOKEN/"
        self.connection = httplib.HTTPConnection("%s:%d" % (self.server, self.port))