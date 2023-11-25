CLIENT_ID="bf0c7fe20a5df4a81804"
CLIENT_SECRET="04fcca19d2798fb0c9e77cfc0d68c5e99ee8946d"

from requests_oauthlib import OAuth2Session
import json

authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'
github = OAuth2Session(CLIENT_ID)
authorization_url, state = github.authorization_url(authorization_base_url)
print('Please go here and authorize,', authorization_url)
redirect_response = input('Paste the full redirect URL here:')
github.fetch_token(token_url, client_secret=CLIENT_SECRET,authorization_response=redirect_response)
response = github.get('https://api.github.com/user')
print(response.content.decode())
dict_response = json.loads(response.content.decode())
for key, value in dict_response.items():
    print(key, '-->', value)
