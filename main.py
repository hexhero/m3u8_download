''' TEST SUCCESS '''
import m3u8
import requests
from Crypto.Cipher import AES
import os
import subprocess


url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671762462zm6iOK.m3u8?sign=25adc60e759f5d29690105bdb2f4e691&t=6419a6b1'
ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/c7079300243791575997343670/drm/%s&sign=3c892d3b8e578bd434ebf7ee8f124642&t=641a4f71&us=DvMShnofgt'

'''
t.key.buffer, t.iv.buffer
AES-128
self.demuxer.decrypter.key / new Uint8Array(self.demuxer.decrypter.key)
'''
key = bytearray((32, 223, 128, 58, 213, 126, 68, 24, 100, 99, 174, 71, 45, 128, 178, 179))
iv = b'\x00' * 16
aes = AES.new(key, AES.MODE_CBC, iv)

output_ts = "temp.ts"
output_path = 'E:/DEVLOP/m3u8_download/video/'
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
            i=i+1
            v_url = ts_url % uri
            print(f'download ts [{i}]: ' + v_url)
            r = requests.get(v_url)
            f.write(aes.decrypt(r.content))
            # f.write(r.content)
            # time.sleep(1)
            # break
    
def decrypt():
    # 使用FFmpeg处理文件
    subprocess.call(['C:/Users/Admin/scoop/apps/ffmpeg/6.0/bin/ffmpeg', '-i', output_ts, '-c:v', 'copy', '-c:a', 'copy', os.path.join(output_path, 'output_processed.mp4')])

download_ts()
decrypt()