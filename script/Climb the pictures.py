# -*- coding: UTF-8 -*-s


"""
    Author:
        Mr guo
    python 2.7
"""


import requests
from bs4 import BeautifulSoup
import re

from contextlib import closing
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import os
import urllib
from tqdm import tqdm
import time


# 获取章节列表
def getcharlist():
    target_url = "https://www.dmzj.com/info/yaoshenji.html"
    req = requests.get(url=target_url)
    potest = req.text
    bs = BeautifulSoup(potest,'lxml')
    charter = bs.find('ul',class_='list_con_li autoHeight')
    charters = charter.find_all('a')
    charters_name = []
    charters_list = []
    for i in charters:
        href = i.get('href')
        ch_name = i.text
        charters_name.append(ch_name)
        charters_list.append(href)
    data = [charters_name,charters_list]
    return data




# 获取图片真实的物理地址
def getimageurl(target_url1):
    # target_url1 = 'https://www.dmzj.com/view/yaoshenji/41917.html'
    r = requests.get(url=target_url1)
    html3 = BeautifulSoup(r.text,'lxml')
    script_info = html3.script
    pics = re.findall('\d{13,14}',str(script_info))
    for dis,picx in enumerate(pics):
        if len(picx) == 13:
            pics[dis] = picx + '0'
    pics = sorted(pics,key=lambda x:int(x))
    chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]
    chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]
    chart_d_list = []
    for pic in pics:
        if pic[-1] == '0':
            imgurl = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
        else:
            imgurl = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
        chart_d_list.append(imgurl)
    return chart_d_list


# 根据物理地址，构造用户信息，爬取图片
def downimg(url,urllist,save_dir):
    do_headers = {
        'Referer':url
    }
    for i,imurl in enumerate(urllist):
        # imurl = 'https://images.dmzj.com/img/chapterpic/3059/14237/14395217739069.jpg'
        # urllib.urlretrieve(imurl,'1.img')
        with closing(requests.get(imurl,headers=do_headers,stream=True)) as response:
            cun_zise = 1024
            content_size = int(response.headers['content-Length'])
            if response.status_code == 200:
                # print '文件大小:%0.2f kb' %(content_size/cun_zise)
                picname = '%03d.jpg' %(i+1)
                img_save_dic_dir = os.path.join(save_dir,picname)
                with open(img_save_dic_dir,'wb') as f:
                    for data in response.iter_content(chunk_size=cun_zise):
                        f.write(data)
            else:
                print('连接异常')
        # print '下载完成'





if __name__ == '__main__':

    comic_name = '妖神记'
    if comic_name not in os.listdir('./'):
        os.mkdir(comic_name)
#     获取章节，名称列表
    datas = getcharlist()
    for i,url in enumerate(tqdm(datas[1])):
        comic_charter_name = datas[0][i]
        phyaddresslist = getimageurl(url)
        while '.' in comic_charter_name:
            comic_charter_name = comic_charter_name.replace('.','')
        charter_save_dir = os.path.join(comic_name,comic_charter_name)
        if charter_save_dir not in os.listdir(comic_name):
            os.mkdir(charter_save_dir)
        downimg(url,phyaddresslist,charter_save_dir)
        time.sleep(10)

