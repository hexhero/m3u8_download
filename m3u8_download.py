''' TEST SUCCESS '''
import m3u8
import requests
from Crypto.Cipher import AES
import os
import subprocess
import process_bar as bar
import logging

ffmpeg_path = 'C:/Users/Admin/scoop/apps/ffmpeg/6.0/bin/ffmpeg'
# ffmpeg_path = 'ffmpeg'

logging.basicConfig(filename='error.log', level=logging.ERROR)

class download():
    def __init__(self, m3u8_url:str, ts_url:str, key:tuple, iv=b'\x00' * 16):
        self.m3u8_url = m3u8_url
        self.ts_url = ts_url
        self.key = key 
        self.iv = iv                  
        self.plist = m3u8.load(m3u8_url)
        self.aes = AES.new(bytearray(key), AES.MODE_CBC, iv)
        self.key_url = self.plist.keys[0].absolute_uri + '&uid=u_640e935553be0_NaRrZ4fb9z'
        
    def download_ts(self,output_ts):
        urilist = self.plist.segments.uri
        # download ts list
        with open(output_ts, "wb") as f:
            i = 0
            size = len(urilist)
            for uri in urilist:
                bar.progress_bar(i, size)
                i=i+1
                v_url = self.ts_url.format(uri)
                r = requests.get(v_url)
                if r.status_code == 200:
                    f.write(self.aes.decrypt(r.content))
                else:
                    print(f'error: {r.status_code}: {r.content}')
                    logging.error(f"download ts error, URI:[{uri}] ERROR: {r.status_code} - {r.content}")
        
    def decrypt(self, output_ts, output_path):
        # 使用FFmpeg处理文件
        subprocess.call([ffmpeg_path, '-i', output_ts, '-c:v', 'copy', '-c:a', 'copy', output_path])
        
        