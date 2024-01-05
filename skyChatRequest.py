# -*- coding: utf-8 -*-


import requests
import time
import hashlib
import json

API_HOST = 'sky-api.singularity-ai.com'
url = f'https://{API_HOST}/saas/api/v4/generate'
app_key = '0ad41f454423a59c0102e82f381a38e5'        # 这里需要替换你的APIKey
app_secret = 'c07df73d0571f4414bd4da9b4510dde48a24eb9b5c11398d'  # 这里需要替换你的APISecret
timestamp = str(int(time.time()))
sign_content = app_key + app_secret + timestamp
sign_result = hashlib.md5(sign_content.encode('utf-8')).hexdigest()


# 设置请求头，请求的数据格式为json
headers={
    "app_key": app_key,
    "timestamp": timestamp,
    "sign": sign_result,
    "Content-Type": "application/json",
    "stream": "true" # or change to "false" 不处理流式返回内容
}

# 设置请求URL和参数
data = {
    "messages": [
        {
            "role": "system",
            "content": "你的名字叫做小奇，是一个智能AI助手"
        },
        {
            "role": "user",
            "content": "给我一个赚取10w的方法"
        }
    ],
    "model": "SkyChat-MegaVerse"
}

# 发起请求并获取响应
response = requests.post(url, headers=headers, json=data, stream=True)

# 处理响应流
for line in response.iter_lines():
    if line:
        # 处理接收到的数据
        print(line.decode('utf-8'))