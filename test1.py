'''
下载单个ts解密并合并
'''

import m3u8
import requests
from Crypto.Cipher import AES
import time
import os
import subprocess

output_ts = "temp.ts"
output_path = 'D:/leoyang/app/m3u8/'
# m3u8 url
url = 'ttps://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1672031192sn56HN.m3u8?sign=0eb4e9e46b3d2fc34b933a2b28ac7c02&t=64196ace'
plist = m3u8.load(url)
key_url = plist.keys[0].absolute_uri + '&uid=u_640e935553be0_NaRrZ4fb9z'
print("[key_url] " + key_url)
response = requests.get(key_url)
if(response.status_code != 200):
    print('getKeyError')
    exit()
key = response.content

# 保存key
with open('key','wb') as k:
    k.write(key)

iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
aes = AES.new(key, AES.MODE_CBC, iv)

def download_ts():
    urilist = plist.segments.uri

    # download ts list
    with open(output_ts, "wb") as f:
        for uri in urilist:
            v_url = f'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/c214e83f243791575997103873/drm/{uri}&sign=bc0b0cc1d388d14ace5e674e29380c06&t=6419f4cc&us=oXNGkiNAZy'
            print('download: ' + v_url)
            r = requests.get(v_url)
            f.write(aes.decrypt(r.content))
            f.write(r.content)
            # time.sleep(1)
            break
    
def decrypt():
    # 使用FFmpeg处理文件
    subprocess.call(['ffmpeg', '-i', output_ts, '-c:v', 'copy', '-c:a', 'copy', os.path.join(output_path, 'output_processed.mp4')])

download_ts()
decrypt()