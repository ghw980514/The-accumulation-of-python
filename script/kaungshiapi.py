# -*- coding: UTF-8 -*-s
import requests
import json
import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt



beatu_url = 'https://api-cn.faceplusplus.com/facepp/v2/beautify'
bea_key = 'OUo7TsbrdorpNuEVTeDnp_WDXGcZAeJp'
bea_secret = '7S6uqCqkqGLbuS29oBPmpN-bBffmx3wQ'


# 可选参数，不填写，默认50
# 美白程度 0 - 100
whitening = 80
# 磨皮程度 0 - 100
smoothing = 80
# 瘦脸程度 0 - 100
thinface = 20
# 小脸程度 0 - 100
shrink_face = 50
# 大眼程度 0 - 100
enlarge_eye = 50
# 去眉毛程度 0 - 100
remove_eyebrow = 50
# 滤镜名称，不填写，默认无滤镜
filter_type = ''


image_url = './timg.jpeg'
f = open(image_url,'rb')
# 转base64
image64 = base64.b64encode(f.read())


data = {
    'api_key':bea_key,
    'api_secret':bea_secret,
    'image_base64':image64,
    'whitening': whitening,
    'smoothing': smoothing,
    'thinface': thinface,
}

res = requests.post(beatu_url,data=data)
html = res.text
html1 = json.loads(html)

# 解析base64图片

base_data = html1['result']
imadata = base64.b64decode(base_data)
npaerr = np.frombuffer(imadata,np.uint8)
img_res = cv2.imdecode(npaerr,cv2.IMREAD_COLOR)
im_bsd = cv2.cvtColor(img_res,cv2.COLOR_RGB2BGR)

img = cv2.imread(image_url)
img_BGR = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


# 显示图片
fig,aix = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(10,10))
aix[0].imshow(im_bsd)
aix[1].imshow(img_BGR)
plt.show()