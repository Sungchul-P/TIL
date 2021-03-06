import sys
import requests
import base64
import json
import logging
import time
import pymysql
import csv

clientID = ""
clientSecret = ""

host = "192.168.56.1"
port = 3306
username = "spotify"
database = "spotify"
password = "1234"

def main():

    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True)
        cursor = conn.cursor()
    except:
        logging.error("could not connect to MySQL")
        sys.exit(1)

    headers = getHeaders(clientID, clientSecret)

    # Spotify Search API
    artists = []
    with open('artist_list.csv', encoding='utf8') as f:
        raw = csv.reader(f)
        for row in raw:
            artists.append(row[0])

    for a in artists:
        params = {
            'q': a,
            'type': 'artist',
            'limit': '1'
        }
    
        try:
            r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
        
        except:
            logging.error(r.text)
            sys.exit(1)

        raw = json.loads(r.text)

        artist = {}
        
        try:
            artist_raw = raw['artists']['items'][0]
            if artist_raw['name'] == params['q']:
                artist.update(
                    {
                        'id': artist_raw['id'],
                        'name': artist_raw['name'],
                        'followers': artist_raw['followers']['total'],
                        'popularity': artist_raw['popularity'],
                        'url': artist_raw['external_urls']['spotify'],
                        'image_url': artist_raw['images'][0]['url']
                    }
                )
                insertRow(cursor, artist, 'artists')
        except:
            logging.error('NO ITEMS FROM SEARCH API')
            continue

    conn.commit()
    sys.exit(0)
    

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

    # print(r.status_code) # 200
    # print(r.text) # {"access_token":"BQApd...H6W6U","token_type":"Bearer","expires_in":3600,"scope":""}

    accessToken = json.loads(r.text)['access_token']

    # AccessToken을 헤더에 대입
    headers = {
        "Authorization": "Bearer {}".format(accessToken)
    }

    return headers

def insertRow(cursor, data, table):

    placeholders = ', '.join(['%s'] * len(data)) # '%s', '%s', '%s' ...
    columns = ', '.join(data.keys())
    key_placeholders = ', '.join(['{0}=%s'.format(k) for k in data.keys()])
    sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON DUPLICATE KEY UPDATE %s" % (table, columns, placeholders, key_placeholders)
    cursor.execute(sql, list(data.values()) * 2)


if __name__ == "__main__":
    main()