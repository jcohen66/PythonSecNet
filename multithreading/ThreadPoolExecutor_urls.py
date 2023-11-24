"""
Among the main advantages provided by these modules, we can highlight that they facilitate
the use of shared memory by allowing access to the state from another context and are the best
option when our application needs to carry out several I/O operations simultaneously.
"""

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

url_list = ["http://www.python.org", "http://www.google.com", "http://packtpub.com", "http://www.yahoooo.com"]

def request_url(url):
    html = requests.get(url, stream=True)
    return url + "-->" + str(html.status_code)

process_list = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for url in url_list:
        process_list.append(executor.submit(request_url, url))

for task in as_completed(process_list):
    print(task.result())