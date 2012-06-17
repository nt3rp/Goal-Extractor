#!/usr/bin/python2
import sys
from oauth import oauth
from fortytwo_goals import FortyTwoGoals
from settings import APP_KEY, APP_SECRET

CALLBACK_URL = ""

def main():
    # Setup
    client   = FortyTwoGoals()
    consumer = oauth.OAuthConsumer(APP_KEY, APP_SECRET)
    signature_method_plaintext = oauth.OAuthSignatureMethod_PLAINTEXT()
    #signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()

    # Get Request Token
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, callback=CALLBACK_URL, http_url=client.request_token_url)
    oauth_request.sign_request(
        signature_method_plaintext, consumer, None)
    token = client.fetch_request_token(oauth_request)

    # Authorize token
    oauth_request = oauth.OAuthRequest.from_token_and_callback(
        token=token, http_url=client.authorization_url)
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

if __name__ == "__main__":
    sys.exit(main())
