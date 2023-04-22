''' TEST SUCCESS '''
import m3u8
import requests
from Crypto.Cipher import AES
import os
import subprocess

'''
t.key.buffer, t.iv.buffer
AES-128
self.demuxer.decrypter.key / new Uint8Array(self.demuxer.decrypter.key)
'''

# 《中医哲学基础》第一讲：中医学的整体观
# url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671689723dHWtZQ.m3u8?sign=086f0cd777d7e24fdecebf8a8d815783&t=64428ca6'
# ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/c214e83f243791575997103873/drm/%s&sign=159c885e3922682a040093ee305b0407&t=64433566&us=WgEGifVZeA'
# key = (195, 43, 125, 241, 83, 116, 226, 252, 58, 86, 177, 4, 76, 132, 145, 40)

# output_ts = "ts/1-1.ts"
# output_path = 'video/1/1.mp4'

iv = b'\x00' * 16
plist = None
aes = None

# m3u8 url
def init(url, key):
    global plist
    global aes
    global key_url
    plist = m3u8.load(url)
    aes = AES.new(bytearray(key), AES.MODE_CBC, iv)
    key_url = plist.keys[0].absolute_uri + '&uid=u_640e935553be0_NaRrZ4fb9z'
# print("[key_url] " + key_url)
# response = requests.get(key_url)
# if(response.status_code != 200):
#     print('getKeyError')
#     exit()
# key = response.content


def download_ts(ts_url,output_ts):
    urilist = plist.segments.uri
    
    # download ts list
    with open(output_ts, "wb") as f:
        i = 0
        for uri in urilist:
            i=i+1
            v_url = ts_url % uri
            print(f'download ts [{i}]')
            r = requests.get(v_url)
            f.write(aes.decrypt(r.content))
            # f.write(r.content)
            # time.sleep(1)
            # break
    
def decrypt(output_ts, output_path):
    # 使用FFmpeg处理文件
    subprocess.call(['C:/Users/Admin/scoop/apps/ffmpeg/6.0/bin/ffmpeg', '-i', output_ts, '-c:v', 'copy', '-c:a', 'copy', output_path])

# download_ts()
# decrypt()