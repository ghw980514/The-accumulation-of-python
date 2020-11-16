# -*- coding: UTF-8 -*-s
import re


# def Getlogdata():
#     file_path_name = ""
#     while True:
#         file_path_name = raw_input("请输入文件路径名称：")
#         if len(file_path_name) == 0:
#             flag = raw_input("您输入的文件名或关键子为空，输出c重试，q退出程序：")
#             if flag == 'q':
#                 return
#             elif flag == 'c':
#                 continue
#         else:
#             break
#     fo = open(file_path_name, 'rb')
#     data = []
#     k_list = []
#
#     for line in fo.readlines():  # 依次读取每行
#         line = line.strip("")  # 去掉每行头尾空白
#         # print "读取的数据为： %s" % (line)
#         if "detail_threat_list_mcs=" in line:
#             ip = re.findall(r'client_ip="(.+?)"', line)
#             if ip not in k_list:
#                 v_dict = {}
#                 k_list.append(ip)
#                 v_type = re.findall(r'virus_type="(.+?)"', line)
#                 v_name = re.findall(r'virus_name="(.+?)"', line)
#                 v_dict['ip'] = ip
#                 v_dict['v_type'] = v_type
#                 v_dict['v_name'] = v_name
#                 data.append(v_dict)
#                 # print k_list
#                 # print v_type, v_name
#                 # print v_dict
#                 # print data
#             else:
#                 v_type = re.findall(r'virus_type="(.+?)"', line)
#                 v_name = re.findall(r'virus_name="(.+?)"', line)
#
#                 if v_dict['ip'] == ip:
#                     v_dict['v_type'].append(v_type)
#                     v_dict['v_name'].append(v_name)
#
#     # # return data
#     # print data
#     # # print k_list
#     # print type(data)
#
#
#
#
# if __name__ == '__main__':
#     Getlogdata()



import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import lxml
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

def get_content(target):
    # target = 'https://www.xsbiquge.com/15_15338/8549128.html'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html1 = req.text
    # print req.text
    bs  = BeautifulSoup(html1,'lxml')
    test1 = bs.find('div',id= 'content')
    test2 = test1.text.strip().split('&nbsp;'*4)
    return test2

if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = './元尊.txt'
    target = 'https://www.xsbiquge.com/78_78513'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html2 = req.text
    # print req.text
    bs  = BeautifulSoup(html2,'lxml')
    charter = bs.find('div',id= 'list')
    charters = charter.find_all('a')
    for i in tqdm(charters):
        url = server + i.get('href')
        charter_name = i.string
        contents = get_content(url)
        # print  contents
        with open(book_name,'a',encoding='utf-8') as f:
            f.write(charter_name)
            f.write('/n')
            f.write('\n'.join(contents))
            f.write('\n')







