#!/usr/bin/python3
#http request with proxy
import requests

proxies = {
   'http': 'http://127.0.0.1:8080',
}

url = 'http://127.0.0.1/'

info = {'offsec':'offsec'}
post = requests.post(url, data = info, proxies=proxies)
print(post.text)
