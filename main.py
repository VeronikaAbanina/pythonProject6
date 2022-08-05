import requests
import json

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

text = json.loads(requests.get(url).content)

Hulk = []
for Hulk in text:
    if Hulk['name'] == 'Hulk':
        intel_Hulk = int(Hulk['powerstats']['intelligence'])

Captain = []
for Captain in text:
    if Captain['name'] == 'Captain America':
        intel_Captain = int(Captain['powerstats']['intelligence'])

Thanos = []
for Thanos in text:
    if Thanos['name'] == 'Thanos':
        intel_Thanos = int(Thanos['powerstats']['intelligence'])

intel_dict = {'Hulk': intel_Hulk, 'Captain': intel_Captain, 'Thanos': intel_Thanos}

print(f'{max(intel_dict)} - самый умный супергерой')