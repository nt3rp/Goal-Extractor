#!/usr/bin/python2
import sys
from oauth import oauth
from fortytwo_goals import FortyTwoGoals
from settings import APP_KEY, APP_SECRET

def setup(client, consumer):
    """ Get everything ready to make requests
    """
    signature_method_plaintext = oauth.OAuthSignatureMethod_PLAINTEXT()

    # Get Request Token
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, http_url=client.request_token_url)
    oauth_request.sign_request(
        signature_method_plaintext, consumer, None)
    token = client.fetch_request_token(oauth_request)

    # Authorize token
    url = client.authorization_url#.replace("$REQUEST_TOKEN", token.key)
    oauth_request = oauth.OAuthRequest.from_token_and_callback(
        token=token, http_url=url)
    response = client.authorize_token(oauth_request)
    import urlparse
    query = urlparse.urlparse(response)[4]
    params = urlparse.parse_qs(query, keep_blank_values=False)
    verifier = params['oauth_verifier'][0]

    # Get Access Token
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, token=token, verifier=verifier, http_url=client.access_token_url)
    oauth_request.sign_request(signature_method_plaintext, consumer, token)
    token = client.fetch_access_token(oauth_request)

    return token

def main():
    client   = FortyTwoGoals()
    consumer = oauth.OAuthConsumer(APP_KEY, APP_SECRET)

    token = setup(client, consumer)

    signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, token=token, http_method='GET', http_url="/v1/goals/")
    oauth_request.sign_request(signature_method_hmac_sha1, consumer, token)

    params = client.access_resource(oauth_request)
    print(params)

if __name__ == "__main__":
    sys.exit(main())
