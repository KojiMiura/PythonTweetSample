#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session

#CK = 'XXXXXXXXXXXXXXXXXXXXXX'                             # Consumer Key
#CS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Consumer Secret
#AT = 'XXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # Access Token
#AS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'         # Accesss Token Secert

URL = "https://api.twitter.com/1.1/statuses/update.json"

def tweet(text):
    params = {"status": text}

    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(URL, params = params)

    return req.status_code

if __name__ == '__main__':
    print tweet("Test tweet, post by python!! #python")

