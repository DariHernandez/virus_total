#! python3

"""
Conect with Virus Total Api to scan local files
"""

import requests, pprint

# Api key
api_key = "598f626e8039d175f0b2cce97899569331deb3d95869c4215b4027c6653fcc83"

# Absolute or relative path of the file
file = "example.txt"

# Analize file
url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {'apikey': api_key}
files = {'file': ('', open(file, 'rb'), open(file, 'r'))}
response = requests.post(url, files=files, params=params)

# Get the key of the report
sha1 = response.json()["sha1"]

# Get report of file
url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey': api_key, 'resource': sha1}
response = requests.get(url, params=params)

# Print report
pprint.pprint (response.json())