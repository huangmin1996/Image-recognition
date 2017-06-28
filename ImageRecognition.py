# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: Image-recognition
# author: "Lei Yong" 
# creation time: 2017/6/28 0028 13:45
# Email: leiyong711@163.com

import time
import urllib2
import json

data = []


def img_recognition(filename):
    # 协议URL
    http_url = 'https://api-cn.faceplusplus.com/imagepp/v1/recognizetext'
    # 公钥
    key = "m_JZUUs-CzSzKsaqZa_TOAD7PMl4tv6r"
    # 密钥
    secret = "SqeJQDQ_ZBpKKwxJUEgpq0fv-FY6OS6N"
    # 参数协议分割标识
    boundary = '-%s' % hex(int(time.time() * 1000))

    # 制作协议包
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('image_file', filename))
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(open(filename, 'rb').read())
    data.append('--%s--\r\n' % boundary)
    # print data

    # 发送POST请求
    http_body = '\r\n'.join(data)
    req = urllib2.Request(http_url)
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    # print http_body
    req.add_data(http_body)
    resp = urllib2.urlopen(req, timeout=5)
    # 获得结果
    qrcont = resp.read()
    # 打印结果
    ps = json.loads(qrcont)
    acc = ps['result']
    # print acc
    return acc[0]['value']
