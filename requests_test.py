import requests

r = requests.get("https://github.com/favicon.ico")
with open('requests_test_favicon.ico', 'wb') as f:
    f.write(r.content)
