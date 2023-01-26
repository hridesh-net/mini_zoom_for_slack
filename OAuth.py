from flask import Flask, abort, request

import os
# from uuid import uuid4
import requests
import requests.auth
import urllib

# client_id = "AKvjQp2pRY6QtfhyTceKLg"

CLIENT_ID = "AKvjQp2pRY6QtfhyTceKLg"  # Fill this in with your client ID
CLIENT_SECRET = "s1TTa1ZaTKXb5JdK21dm62rjW5U16Xui"  # Fill this in with your client secret
REDIRECT_URI = "http://localhost:65010/zoom_callback"

app = Flask(__name__)


@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with Zoom</a>'
    return text % make_authorization_url()


def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks

    params = {"client_id": CLIENT_ID,
              "response_type": "code",
              "redirect_uri": REDIRECT_URI}
    url = "https://zoom.us/oauth/authorize?" + urllib.parse.urlencode(params)
    return url


@app.route('/zoom_callback')
def zoom_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error

    code = request.args.get('code')
    access_token = get_token(code)
    # Note: In most cases, you'll want to store the access token, in, say,
    # a session for use in other parts of your web app.
    meeting_list = server().getAttendieList(access_token)
    print(meeting_list)
    return "Your user info is: %s" % get_username(access_token)


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI,
                 "scope": "meeting:read:admin"}

    response = requests.post("https://zoom.us/oauth/token",
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    # print(token_json)
    print("\n\n")
    access_token = token_json['access_token']
    # print(access_token)
    return token_json["access_token"]


def get_username(access_token):
    headers = {"Authorization": "bearer " + access_token}
    response = requests.get("https://api.zoom.us/v2/users/me", headers=headers)
    me_json = response.json()
    # meeting_list = server().getAttendieList(access_token)
    return me_json


class server:

    def getAttendieList(self, Token):
        response = requests.get(f'https://api.zoom.us/v2/users/me/meetings', headers={'Authorization': Token})
        return response.json()
    def createJSONtoCSV(self,JSON):
        output_csv_file = 'csv_file.csv'
        JSON.to_csv(output_csv_file, index=False)
        #varriable in a string

if __name__ == '__main__':
    app.run(debug=True, port=65010)