import httplib
from oauth.client import SimpleOAuthClient

class FortyTwoGoals(SimpleOAuthClient):
    def __init__(self):
        self.server = "api.42goals.com"
        self.port = 80
        self.request_token_url = "/v1/oauth/request_token/"
        self.access_token_url = "/v1/oauth/access_token/"
        self.authorization_url = "/settings/authorize/$REQUEST_TOKEN/"
        self.connection = httplib.HTTPConnection("%s:%d" % (self.server, self.port))

    def get_authorize_url(self, oauth_request):
        oauth_token = oauth_request.parameters.get("oauth_token")
        url =  oauth_request.http_url.replace("$REQUEST_TOKEN", oauth_token)
        return url

    def authorize_token(self, oauth_request):
        # Now, we get 'not authorized' instead of 'not found'
        conn = httplib.HTTPConnection("42goals.com:80")
        url = self.get_authorize_url(oauth_request)
        conn.request("POST", url)
        response = conn.getresponse()
        print response.status, response.reason
        response_str = response.read()
        return response_str