# -*- coding: UTF-8 -*-s

#
import requests
from bs4 import BeautifulSoup
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import ffmpy
from multiprocessing.dummy import Pool as TThreadPool
import os

search_list = {}
video_url = 'C:\\Users\\Administrator\\Desktop\\video'


def getDetails(content):
    search_name = content
    sreach_url = 'http://www.jisudhw.com/index.php'
    search_params = {
        'm':'vod-search'
    }
    search_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Referer': 'http://www.jisudhw.com/',
        'Origin': 'http://www.jisudhw.com',
        'Host': 'www.jisudhw.com'
    }
    serach_datas = {
        'wd': search_name,
        'submit': 'search'
    }

    r = requests.post(url=sreach_url,params=search_params,headers=search_headers,data=serach_datas)

    # r.encoding('utf-8')
    server = 'http://www.jisudhw.com'
    search_html = BeautifulSoup(r.text,'lxml')
    search_span = search_html.find_all('span',class_='xing_vb4')
    for i in search_span:
        url = server + i.a.get('href')
        sp_name = i.a.string
    return url




def getvideolink(s_url):
    detail_url = s_url
    r = requests.get(url=detail_url)
    detail_df = BeautifulSoup(r.text,'lxml')
    num = 1

    for eauc in detail_df.find_all('input'):
        if 'm3u8' in eauc.get('value'):
            url = eauc.get('value')
            if url not in search_list.keys():
                search_list[url] = num
            num += 1
    # global search_list
    # return search_list




# 下载视频
def downvideo(url):
    num = search_list[url]
    name = os.path.join(video_url,'%03d.mp4' %num)
    ffmpy.FFmpeg(executable='D:\\360down\\ffmpeg-20200729-cbb6ba2-win64-static\\bin\\ffmpeg.exe',inputs={url: None}, outputs={name:None}).run()


#
if __name__ == '__main__':
    search_content = '越狱第一季'
    videoinfo = getDetails(search_content)
    getvideolink(videoinfo)
    if not os.path.exists(video_url):
        os.mkdir(video_url)
    pool = TThreadPool(3)
    result = pool.map(downvideo,search_list.keys())
    pool.close()
    pool.join()


