import requests

r = requests.get("https://api.ipify.org?format=json", proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')).json()['ip']
print(r)