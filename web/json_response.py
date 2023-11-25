import urllib.request
import json

url= "http://httpbin.org"
with urllib.request.urlopen(url) as response_json:
    data_json = json.loads(response_json.read().decode("utf-8"))
    print(data_json)
