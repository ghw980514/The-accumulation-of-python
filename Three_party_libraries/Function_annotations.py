'''
title: 函数注释 typing
description:没有实际意义，用来表明函数输入和返回的类型,支持python3.5以上版本使用
import: from typing import List
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation :
'''

from typing import Tuple,List,Set
def sou(a:int,b:str='3') -> bool:
    if a > 6:
        print(a+int(b))
        return True
    else:
        print(str(a)+b)
        return False


def gou(q:int,w:str) -> Tuple[List[str],str or int,Set]:
    list1 = []
    list1.append(w)
    list2 = set(list1)
    return list1,1,list2



if __name__ == '__main__':
    it = sou(1)
    print(it)
    iu = gou(3,'rrr')
    print(iu)
# 填入类型不正确时，pycharm会有类型提示
# 可以提示返回值中list等类型的类型提示
# typing模块支持的类型
    # int,long,float：整型，长整型，浮点型
    # bool,str：布尔型，字符串类型
    # List,Tuple,Dict,Set：列表，元组，字典，集合
    # Iterable,Iterator：可迭代器，迭代器类型
    # Generator：生成器类型
# return:
    # 13
    # False
    # (['rrr'], 1, {'rrr'})

# a:int  提示a的参数类型是int，但输入别的类型也不会报错
# -> bool    提示返回值是bool类型，但是返回别的类型也不会报错
# b:str='3'    ='3' 为b设置默认值