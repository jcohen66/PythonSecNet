import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input("Enter your username: ")
response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(username, getpass()))
print("Response.status_code: " + str(response.status_code))
if response.status_code == 200:
    print("Login successful:", response.text)