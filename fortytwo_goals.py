import httplib
from oauth.client import SimpleOAuthClient

class FortyTwoGoals(SimpleOAuthClient):
    def __init__(self):
        self.server = "api.42goals.com"
        self.port = 80
        self.request_token_url = "/v1/oauth/request_token"
        self.access_token_url = "/v1/oauth/access_token"
        self.authorization_url = "http://42goals.com/settings/authorize/$REQUEST_TOKEN/"
        self.connection = httplib.HTTPConnection("%s:%d" % (self.server, self.port))

    def authorize_token(self, oauth_request):
        # For whatever reason, 42goals doesn't have
        # everything under api.42goals.com. So, we need
        # to use a new connection temporarily.

        oauth_token = oauth_request.parameters.get("oauth_token")
        url = oauth_request.http_url.replace("$REQUEST_TOKEN", oauth_token)

        conn = httplib.HTTPConnection("42goals.com:80")
        conn.request(oauth_request.http_method, url)
        response = conn.getresponse()

#        url = oauth_request.to_url()
#        self.connection.request(oauth_request.http_method, url)
#        response = self.connection.getresponse()

        str_response = response.read()
        return str_response