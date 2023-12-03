import requests
logins = []
with open("./logins.txt", "r") as filehandle:
    for line in filehandle:
        login = line[:-1]
        logins.append(login)
domain = "http://testphp.vulnweb.com"
for login in logins:
    print("Checking: " + domain + "/" + login)
    response = requests.get(domain + "/" + login)
    if response.status_code == 200:
        print("Found: " + domain + "/" + login)
        break
