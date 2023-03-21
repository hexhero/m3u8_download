''' TEST SUCCESS '''
import m3u8
import requests
from Crypto.Cipher import AES
import os
import subprocess


url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671761825S7rhMl.m3u8?sign=30b79b1912679fbc069baea30070f309&t=64198791'
ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/f0401e1f243791577233942895/drm/%s&sign=8bcaacc700b40a4ca9d767b5aef3493f&t=641a3051&us=lviHGpDWQu'

'''
t.key.buffer, t.iv.buffer
AES-128
self.demuxer.decrypter.key / new Uint8Array(self.demuxer.decrypter.key)
'''
key = bytearray((219, 167, 178, 77, 80, 156, 20, 53, 206, 215, 24, 246, 34, 113, 105, 67))
iv = b'\x00' * 16
aes = AES.new(key, AES.MODE_CBC, iv)

output_ts = "temp.ts"
output_path = 'D:/leoyang/app/m3u8/'
# m3u8 url
plist = m3u8.load(url)
# key_url = plist.keys[0].absolute_uri + '&uid=u_640e935553be0_NaRrZ4fb9z'
# print("[key_url] " + key_url)
# response = requests.get(key_url)
# if(response.status_code != 200):
#     print('getKeyError')
#     exit()
# key = response.content


def download_ts():
    urilist = plist.segments.uri
    
    # download ts list
    with open(output_ts, "wb") as f:
        i = 0
        for uri in urilist:
            v_url = ts_url % uri
            print(f'download ts [{i}]: ' + v_url)
            r = requests.get(v_url)
            f.write(aes.decrypt(r.content))
            # f.write(r.content)
            # time.sleep(1)
            # break
    
def decrypt():
    # 使用FFmpeg处理文件
    subprocess.call(['ffmpeg', '-i', output_ts, '-c:v', 'copy', '-c:a', 'copy', os.path.join(output_path, 'output_processed.mp4')])

download_ts()
decrypt()