import requests

print(requests.__version__)

r1 = requests.get("http://www.google.com")
print(r1.status_code)
