import requests
import json 
from requests import ConnectionError,HTTPError,Timeout
try : 
    url="https://httpbin.org/post"
    url_auth='https://httpbin.org/basic-auth/1111/1111'
    url_delay= "https://httpbin.org/post/delay/5"
    url_pyramid="http://localhost:6543/hello"
   
    params ={
        'id':12,
        "name": "max",
    }
    data={
        "name":"max",
        "age": 20
    }
    headers={
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    auth=("1111","1111")


    res = requests.post(url_pyramid,json=data)
    print(res.json())

    # print(res.text)
    print(res.url)
    #print(res.json())
    #print(res.headers)
except ConnectionError:
    print('找不到伺服器')

    print('沒有發生問題')