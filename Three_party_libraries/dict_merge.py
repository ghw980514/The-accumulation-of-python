'''
title: dict
description : 字典合并的多种方法
import:
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : 
'''


prolife = {'name':'jamesless','age':24}
extinfo = {'gendder':'male'}
# prolife.update(extinfo)
# print(prolife)
# # 字典自带方法

# ----------------------------------------------------------------------------------------------------------------------
#使用深拷贝生成一个新的对象
from copy import deepcopy
newprolife = deepcopy(prolife)
newprolife.update(extinfo)
# print(newprolife)
# ----------------------------------------------------------------------------------------------------------------------
# 使用**可以解包字典，解包完在使用dict或者{}就可以重组成字典
newprolife2 = {**prolife,**extinfo}
newprolife3 = dict(**prolife,**extinfo)
# print(newprolife2)
# print(newprolife3)
# ----------------------------------------------------------------------------------------------------------------------
#使用itertools.chain()内置方法将字典转化成可迭代对象，在使用dict进行转换
import itertools

newprolife4 = dict(itertools.chain(prolife.items(),extinfo.items()))
# print(newprolife4)
# ----------------------------------------------------------------------------------------------------------------------
# 使用 | 操作符，取并集，然后再利用dict函数转换
newprolife5 = dict(prolife.items() | extinfo.items())
# print(newprolife5)

# ----------------------------------------------------------------------------------------------------------------------
# 使用字典解析式
newprolife6 = {k:v for d in [prolife,extinfo] for k,v in d.items()}
print(newprolife6)