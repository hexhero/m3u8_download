import home, re
'''
t.key.buffer, t.iv.buffer
AES-128
self.demuxer.decrypter.key / new Uint8Array(self.demuxer.decrypter.key)
/m3u8|\.ts/
'''

# 《中医哲学基础》第一讲：中医学的整体观
# url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671689723dHWtZQ.m3u8?sign=086f0cd777d7e24fdecebf8a8d815783&t=64428ca6'
# ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/c214e83f243791575997103873/drm/%s&sign=159c885e3922682a040093ee305b0407&t=64433566&us=WgEGifVZeA'
# key = (195, 43, 125, 241, 83, 116, 226, 252, 58, 86, 177, 4, 76, 132, 145, 40)

# output_ts = "ts/1-1.ts"
# output_path = 'video/1/1.mp4'

# 《中医哲学基础》第二讲：中医学的辨证论治观
# url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671689765lJNLhv.m3u8?sign=454452cb21077c8b03ce92e77cc7ce8c&t=644296b5'
# ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/ee246ed5243791577233878220/drm/v.f421220_0.ts?start=0&end=353455&type=mpegts&sign=1515a00415960284f65da20579d984cc&t=64433f75&us=gZBxUkFmxU'
# ts_url = re.sub('v\..*mpegts','%s',ts_url)
# key = (16, 166, 25, 224, 110, 33, 195, 44, 143, 153, 121, 126, 150, 9, 234, 127)

# output_ts = "ts/1-2.ts"
# output_path = 'video/1/2.mp4'

# 《中医哲学基础》第三讲：阴阳学说的形成
url = 'https://pri-cdn-tx.xiaoeknow.com/appzBbFCNAm1880/private_index/1671689946N1za34.m3u8?sign=99bebf516d7780666bcf3616241e5de4&t=64429ade'
ts_url = 'https://c-vod.hw-cdn.xiaoeknow.com/2919df88vodtranscq1252524126/eb62bc3b243791577233718467/drm/v.f421220_0.ts?start=0&end=354207&type=mpegts&sign=d0b9b45ef16bb8493638d07e615eb8c6&t=6443439e&us=HsEbyOPEAE'
ts_url = re.sub('v\..*mpegts','%s',ts_url)
key = (147, 243, 199, 12, 99, 179, 143, 248, 101, 111, 30, 33, 39, 200, 222, 78)

output_ts = "ts/1-3.ts"
output_path = 'video/1/3.mp4'

home.init(url, key)
home.download_ts(ts_url,output_ts)
home.decrypt(output_ts, output_path)