import requests
import json 
from requests import ConnectionError,HTTPError,Timeout
try : 
    url="https://httpbin.org/post"
    url_auth='https://httpbin.org/basic-auth/1111/1111'
    url_delay= "https://httpbin.org/post/delay/5"
    url_pyramid="http://localhost:6543/hello"
    url_example_route="http://localhost:6543/example_route"
    url_example_route2="http://localhost:6543/example_route2"
    url_test_get="http://localhost:6543/get"
    url_test2_post="http://localhost:6543/post"
    params ={
        'id':12,
        "name": "chris",
        "flag" :2
    }
    json_data={
        "chris":"123",
        "max":"332",
        "amy":"123123123qw"
    }   

    res = requests.get(url_test2_post, json=json_data)
    print(res)
    
    if res.status_code == 200:
    # Print the response JSON data
        print(res.json())
    else:
        # Print an error message if the request failed
        print(f"Error: {res.status_code}")

    #print(res.text)
    print(res.url)
    #print(res.json())
    #print(res.headers)
except ConnectionError:
    print('找不到伺服器')

    print('沒有發生問題')