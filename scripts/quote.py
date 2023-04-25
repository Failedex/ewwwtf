#!/usr/bin/python3
import requests
import json

res = json.loads(requests.get("https://api.quotable.io/random/?maxLength=78").text)

print(f"(box :orientation 'v' :space-evenly true (label :text `\"{res['content']}\"`) (label :style 'font-size: 14;' :text `- {res['author']}`))")
