key_url = 'https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=appzBbFCNAm1880&mid=m_Ao6Fu2qwakCzR_zem25z7o&urld=aac2d0ca713c5a876ad679cee071ddab&uid=u_640e935553be0_NaRrZ4fb9z'

import requests

resp = requests.get(key_url);

key_byte = resp.content

# 定义一个空列表，用于存储转换后的数字
result = []

# 遍历字节数组，对每个字节进行转换
for b in key_byte:
    # 使用int()函数转换字节为数字，并将结果存储到列表中
    result.append(int(b))

# 输出转换后的结果
print(result)  # [1, 2, 3, 4]

# [102, 39, 85, 13, 26, 29, 49, 84, 46, 53, 150, 251, 10, 54, 71, 42] 
# [19, 120, 99, 57, 42, 120, 8, 103, 27, 0, 163, 200, 104, 83, 119, 117]
