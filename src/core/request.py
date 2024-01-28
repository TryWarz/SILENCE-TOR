import requests

# Path: src/core/response.py

class request:
    def __init__(self) -> None:
        self.host = requests.get("https://api.ipify.org?format=json", proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')).json()['ip']
