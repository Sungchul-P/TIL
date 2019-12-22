import sys
import requests
import base64
import json
import logging
import time

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

    try:
        r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
    
    except:
        logging.error(r.text)
        sys.exit(1)

    # StatusCode Error Handling
    if r.status_code != 200:
        logging.error(r.text)

        # 429 Code : Too Many Request
        if r.status_code == 429:
            # 대기 시간을 Retry-After로 반환한다.
            retryAfter = json.loads(r.headers)['Retry-After']
            time.sleep(int(retryAfter))

            requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

        # 401 Code : AccessToken expired
        elif r.status_code == 401:
            headers = getHeaders(clientID, clientSecret)
            requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

        else:
            sys.exit(1)

    # Spotify Get an Artist's Albums API
    artistID = "6OwKE9Ez6ALxpTaKcT5ayv"
    r = requests.get("https://api.spotify.com/v1/artists/{id}/albums".format(id=artistID), headers=headers)

    raw = json.loads(r.text)

    total = raw['total']
    offset = raw['offset']
    limit = raw['limit']
    next = raw['next'] # 다음 요청 해야 할 Endpoint

    print("total : {}\noffset : {}\nlimit : {}\nnext : {}".format(total, offset, limit, next))

    albums = []
    print(len(raw['items']))
    albums.extend(raw['items'])

    # 앨범 n 개 정보만 조회
    n = 100
    count = 0
    while count < n and next:
        r = requests.get(raw['next'], headers=headers)
        raw = json.loads(r.text)
        next = raw['next']
        print(next)

        albums.extend(raw['items'])
        count = len(albums)

    print(len(albums))

    # print(r.status_code)
    # print(r.text)
    # print(r.headers)
    

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