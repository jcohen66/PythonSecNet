import requests, json

response = requests.get("http://httpbin.org/get", timeout=5)
print(f"HTTP Status Code: {response.status_code}")
if response.status_code == 200:
    results = response.json()
    for result in results:
        print(result)
    print("Headers Response:")
    for header, value in response.headers.items():
        print(f"{header} --> {value}")
    print("Headers Request:")
    for header, value in response.request.headers.items():
        print(f"{header} --> {value}")
    print(f"Server: {response.headers['server']}")
else:
    print(f"HTTP Error Code: {response.status_code}")
    print(f"HTTP Error Message: {response.text}")


