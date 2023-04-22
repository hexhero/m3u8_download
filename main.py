from m3u8_download import download
import re, json
'''
t.key.buffer, t.iv.buffer
AES-128
self.demuxer.decrypter.key / new Uint8Array(self.demuxer.decrypter.key)
/m3u8|\.ts/
'''

with open('videos.json', encoding='utf-8') as v:
    video = json.loads(v.read())

for d in video['零基础学中医'].items():
    v = d[1]
    if v['download']:
        print(f"下载课程: {v['name']}")
        ts_url = re.sub('v\..*mpegts','{}', v['ts_url'])
        d = download(v['url'], ts_url, v['key'])
        d.download_ts(v['output_ts']); 
        d.decrypt(v['output_ts'], v['output_path'])