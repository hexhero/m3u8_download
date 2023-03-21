import os
import subprocess
from Crypto.Cipher import AES
import requests

m3u8_url = 'your_m3u8_url'
output_path = 'your_output_path'
key_uri = 'your_key_uri'

# 下载m3u8文件
response = requests.get(m3u8_url)
m3u8_content = response.text

# 获取ts文件列表
ts_list = [line.strip() for line in m3u8_content.split('\n') if line.endswith('.ts')]

# 下载并合并ts文件
output_ts = os.path.join(output_path, 'output.ts')
with open(output_ts, 'wb') as f:
    for ts in ts_list:
        ts_url = m3u8_url.rsplit('/', 1)[0] + '/' + ts
        response = requests.get(ts_url)
        f.write(response.content)

# 下载并解密key
response = requests.get(key_uri)
key = response.content

# 解密ts文件
iv = b'\x00' * 16 # 偏移量
aes = AES.new(key, AES.MODE_CBC, iv)
with open(output_ts, 'rb') as f:
    encrypted_data = f.read()

decrypted_data = aes.decrypt(encrypted_data)

# 保存解密后的文件
output_file = os.path.join(output_path, 'output.mp4')
with open(output_file, 'wb') as f:
    f.write(decrypted_data)

# 使用FFmpeg处理文件
subprocess.call(['ffmpeg', '-i', output_file, '-c:v', 'copy', '-c:a', 'copy', os.path.join(output_path, 'output_processed.mp4')])
