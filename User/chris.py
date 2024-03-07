import requests
import json 
from requests import ConnectionError,HTTPError,Timeout
try : 
    url="http://localhost:8000/api"
    url_post="http://localhost:8000/api/api_post"

    params ={
        'id':12,
        "name": "chris",
        "flag" :2
    }
    json={
        "chris":"123",
        "max":"332",
        "amy":"123123123qw"
    }   
    password={
        "account":"kingcall",
        "password":"1111"
    }

    #res = requests.post(url_post,json=json)
    res = requests.get(url,json=json)
    print(res)
    data=res.json()["status"]
    print(data)
   
except ConnectionError:
    print('找不到伺服器')
    print('沒有發生問題')