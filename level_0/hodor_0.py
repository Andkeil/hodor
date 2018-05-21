#!/usr/bin/python3
"""
level_0
"""


import requests

ID = 321
URL = "http://158.69.76.135/level0.php"
package = {
    'id': ID,
    'holdthedoor': 'Submit'
}
for i in range(1024):
    r = requests.post(URL, data=package)
