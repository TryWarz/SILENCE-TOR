from request import request as r
import os

def tor_reload():
    os.system("service tor reload")

def tor_start():
    os.system("service tor start")

