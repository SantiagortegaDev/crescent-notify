#!/usr/bin/env python3

import json
import re
import urllib.request
import html as _html

cookie = ""   # _crescent_session=.....

def props(path):
    """Pide una ruta de Crescent y devuelve los props (dict). Esto ya funciona."""
    req = urllib.request.Request(
        "https://crescent.hackclub.com" + path,
        headers={"Cookie": cookie, "Accept": "text/html"},
    )
    html = urllib.request.urlopen(req).read().decode("utf-8", "replace")
    raw = re.search(r'data-page="app" type="application/json">(.*?)</script>', html, re.S).group(1)
    return json.loads(_html.unescape(raw))["props"]



#   some api responses
#   props("/refuge")["auth"]["user"]        -> name, handle, email, balance
#   props("/projects")["projects"]          -> lista: id, title, status, href
#   props("/projects/385")["project"]       -> status, statusLabel, title
#   props("/projects/385")["shipping"]["pending"]

def main():
    data = props("/projects")     
    print(data)    
    proyectos = data["projects"]       

    for p in proyectos:
        print(p["id"], p["title"], p["status"])


if not cookie:
    raise SystemExit("cookie missing")
main()