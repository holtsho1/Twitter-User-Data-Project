client_key = '' #import your own key here from TwitterAPI
client_secret = '' #import your own secret here from TwitterAPI
access_token = '' #import your own access token from TwitterAPI

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {

    'grant_type': 'client_credentials'
}


auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)


# Check status code okay, should be 200
auth_resp.status_code
#print(auth_resp.status_code)

# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()
#print(auth_resp.json().keys())
