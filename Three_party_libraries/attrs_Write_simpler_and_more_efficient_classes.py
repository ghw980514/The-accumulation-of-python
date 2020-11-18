'''
title: attr
description: attr是一个python包，旨在帮助你编写简单而正确的程序，并且不影响代码的运行速度。他的实际作用是使python类变得更加简单高效，
import: from attr import attrs, attrib
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : pip install attrs,cattrs
'''
# import sys
# # sys.version   #查看python版本

# 首先明确一点，我们现在是装了 attrs 和 cattrs 这两个库，但是实际导入的时候是使用 attr 和 cattr 这两个包，是不带 s 的
# import attr
# attrs     自定义类
# attrib    自定义字段属性

# 例
from attr import attrs,attrib,fields
from cattr import structure,unstructure

# 验证器方法名为is_valid_gender  包含以下三个参数，这三个参数是固定的
# instance：类对象
# attribute：属性名
# value：属性值
# 验证器方法
def is_valid_gender(instance,attribute,value):
    if value > 255:
        raise ValueError(f'{value} is not vaild')

# 转换器方法

# value值是固定的
def to_int(value):
    try:
        return int(value)
    except:
        return None

@attrs
class Color(object):
    red = attrib(type=int,default=0,validator=is_valid_gender)
    green = attrib(type=int,default=0,converter=to_int)
    blue = attrib(type=int,default=0)



if __name__ == '__main__':
    hs = Color(255,255,255)
    print(hs)

# return  :  color(red=255, green=255, blue=255)   按顺序赋值输出，不是一个color对象
# 主要是 attrs 这个修饰符起了作用，然后根据定义的 attrib 属性自动帮我们实现了 __init__、__repr__、__eq__、__ne__、__lt__、__le__、__gt__、__ge__、__hash__ 这几个方法
# __ne__    不等于
#验证使用比较符来对类与类之间进行比较,实际是将类中的color(1,2,3)转化成元祖进行比较
    print(Color(1,2,3) == Color(1,2,3))       #True
    print(Color(1,2,4) > Color(2,3,4))        #False
    print(Color(2,3,4) <= Color(2,3,4))       #True


# 别名
# s = attributes = attrs
# ib = attr = attrib

    print(fields(Color))      #fields输出color类的所有属性和参数 ，可以在attrib设置这些属性
# return :
#     name：属性的名字，是一个字符串类型。
#     default：属性的默认值，如果没有传入初始化数据，那么就会使用默认值。如果没有默认值定义，那么就是NOTHING，即没有默认值。
#     validator：验证器，检查传入的参数是否合法。
#     init：是否参与初始化，如果为False，那么这个参数不能当做类的初始化参数，默认是True。
#     metadata：元数据，只读性的附加数据。
#     type：类型，比如int、str等各种类型，默认为None。
#     converter：转换器，进行一些值的处理和转换器，增加容错性。
#     kw_only：是否为强制关键字参数，默认为False
# 强制关键字参数的赋值必须显示通过关键字传入。如：color(red=255)   'red=' 必须写

# 假如你想让一个参数不初始化，，一直为一个不变的值，那抹将init设为false，并设置default，那抹他就会一直是这个默认值，如果给他传入参数，就会报错

#验证器例：
    print(Color(246,1,1))    # ValueError: 266 is not vaild
    # 官方给出很多的验证器方法可直接调用
    # 例如：age = attrib(validator=validators.instance_of(int))     判断传入的参数是否是整型
    # 而且支持多个验证方法，只要将其放入列表中传入 例：age = attrib(validator=[validators.instance_of(int), is_less_than_100])

# 转换器
#     假如我们应该传入int类型的3而我们传入了str类型的3，报错是不应该的，所以我们可以使用转换器将str转成int


# 序列转化
# cattrs类实现和json之间的序列化和反序列化
# 序列化
    json = unstructure(hs)
    print(json)
# 反序列化
    hx = structure(json,Color)
    print(hx)
# 可用于接收json参数后做处理使用 ，如提交的json表单信息
