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

    # pymysql_csv 파일을 이용해서 DB에 artists 데이터가 있는 상태에서 진행해야 됨.
    cursor.execute("SELECT id FROM artists")
    artists = []
    for (id, ) in cursor.fetchall():
        artists.append(id)

    # 50개씩 끊어서 새로운 리스트로 나눠서 저장
    artist_batch = [artists[i:i+50] for i in range(0, len(artists), 50)]

    artist_genres = []

    # 최대 50개 id에 대해서 한번에 요청할 수 있도록 spotify가 제공함.
    for i in artist_batch:
        ids = ','.join(i)
        URL = "https://api.spotify.com/v1/artists/?ids={}".format(ids)

        r = requests.get(URL, headers=headers)
        raw = json.loads(r.text)

        for artist in raw['artists']:
            for genre in artist['genres']:
                artist_genres.append(
                    {
                        'artist_id': artist['id'],
                        'genre': genre
                    }
                )

    for data in artist_genres:
        insertRow(cursor, data, 'artist_genres')

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