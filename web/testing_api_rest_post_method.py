import requests
data_dictionary = {"id": "0123456789"}
headers = {"Content-Type": "application/json", "Accept": "application/json"}
# Call Post with data and headers
response = requests.post("http://httpbin.org/post", json=data_dictionary)
print("HTTP Status Code: " + str(response.status_code))
print(response.headers)
if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)
    print("Headers Response:")
    for header, value in response.headers.items():
        print(header, '-->', value)
    print("Headers Request:")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
    print("Server: " + response.headers['server'])
else:
    print("HTTP Error Code: " + str(response.status_code))
    print("HTTP Error Message: " + str(response.text))