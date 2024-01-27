import requests

# Path: src/core/response.py

class request:
    def __init__(self):
        self.host = requests.get("https://www.myexternalip.com/raw", proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')).text

    def get(self):
        return self.host
    


















