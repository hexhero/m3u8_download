import m3u8

url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671761825S7rhMl.m3u8?sign=30b79b1912679fbc069baea30070f309&t=64198791'
plist = m3u8.load(url)
key_url = plist.keys[0].absolute_uri + '&uid=u_640e935553be0_NaRrZ4fb9z'

import requests

resp = requests.get(key_url);

key_byte = resp.content

uint8_array = [byte for byte in key_byte]

print(uint8_array)
