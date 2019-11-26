import sys
import requests
import base64
import json
import logging

clientID = ""
clientSecret = ""

def main():
    headers = getHeaders(clientID, clientSecret)

    # Spotify Search API
    params = {
        "q": "AKMU",
        "type": "artist",
        "limit": "5"
    }

    r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

    print(r.status_code)
    print(r.text)
    

def getHeaders(clientID, clientSecret):
    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(clientID, clientSecret).encode("utf-8")).decode("ascii")

    headers = {
        "Authorization": "Basic {}".format(encoded)
    }

    payload = {
        "grant_type": "client_credentials"
    }

    # 인코딩된 Credential 정보로 POST 요청하여 AccessToken 발급
    r = requests.post(endpoint, data=payload, headers=headers)

    print(r.status_code) # 200
    print(r.text) # {"access_token":"BQApd...H6W6U","token_type":"Bearer","expires_in":3600,"scope":""}

    accessToken = json.loads(r.text)['access_token']

    # AccessToken을 헤더에 대입
    headers = {
        "Authorization": "Bearer {}".format(accessToken)
    }

    return headers


if __name__ == "__main__":
    main()