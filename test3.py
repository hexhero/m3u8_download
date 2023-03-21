'''
t.key.buffer, t.iv.buffer
'''

key_arr = (19, 120, 99, 57, 42, 120, 8, 103, 27, 0, 163, 200, 104, 83, 119, 117)
iv_arr = (0,   0,   0,   0,  0,  0,  0,  0,  0,  0,  0,   0,  0,   0,   0,   0)

key = bytearray(key_arr)
iv = bytearray(iv_arr)

from Crypto.Cipher import AES

aes = AES.new(key, AES.MODE_CBC, iv)

with open('aaa.ts', 'rb') as f:
    data = f.read()
    
xxxx =  aes.decrypt(data) 

with open('xx.mp4','wb') as m:
    m.write(xxxx)  
