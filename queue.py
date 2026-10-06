#!/usr/bin/env python3

import json
import re
import urllib.request
import html as _html

cookie = ""             
project_id = ""         


def props(path):
    req = urllib.request.Request("https://crescent.hackclub.com" + path, headers={"Cookie": cookie, "Accept": "text/html"})
    html = urllib.request.urlopen(req).read().decode("utf-8", "replace")
    raw = re.search(r'data-page="app" type="application/json">(.*?)</script>', html, re.S).group(1)
    return json.loads(_html.unescape(raw))["props"]


def main():
    p = props("/projects/" + project_id)
    pendiente = p["shipping"]["pending"]    # None if the project hasn't been shipped yet


    position = pendiente["position"]        
    total = pendiente["depth"]              
    days = pendiente["medianWaitDays"]      

    print(f"posicion: {position}")   
    print(f"total: {total}")
    print(f"days: {days}")



main()