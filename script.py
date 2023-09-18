import requests

print(requests.__version__)

r1 = requests.get("http://www.google.com")
print(r1.status_code)

r2 = requests.get("https://raw.githubusercontent.com/AryanKalwani/404_lab1/main/script.py")
print(r2.text)

