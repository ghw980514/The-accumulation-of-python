'''
title: decorator
description:装饰器
import:
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : 用于为函数添加额外的方法，使代码更加简洁优雅
'''

# 闭包：内部函数对于外部函数作用域里变量的引用，
# 完成对外部函数变量的封装

# 中文在python3中可以做变量名
# 萨达 = 1
# print(萨达)

# def func():   #外部函数
#     a = 1       #外部函数作用域的变量
#     def func1(num):    #内部函数
#         print(a+num)      #对于外部函数的引用，
#     return func1           #返回内部函数，使外部函数执行完成后，内部函数依旧存活
#
#
# var = func()
# var(0)        #接收调用内部函数，直至del var执行，不然内部函数一直存在


# ----------------------------------------------------------------------------------------------------------------------
# 装饰器


# def new(func):
#     a = 1
#     def new_one(*args,**kwargs):
#         print('two')
#         print(1+a)
#         func()
#         print('third')
#         return func(*args,**kwargs)
#     return new_one
#

#
# @new
# def old():
#     print(old.__name__)
#
#
# old()
# 相当于 old = new(old)
# new(old)()
# ----------------------------------------------------------------------------------------------------------------------
# 装饰器带参数
# 内部返回函数不需要加()
# 三层嵌套，
# 最外层来实现接收装饰器穿的参数
# 第二层接收被装饰的函数
# import functools
# def a_func(sex):
#     def b_func(func):
#         @functools.wraps(func)    #作用：因装饰器装饰函数后，被装饰函数的.__name__会变成装饰器内部函数，所以为保证属性值不变的情况下进行装饰，functools.wraps 旨在消除装饰器对原函数造成的影响，即对原函数的相关属性进行拷贝，已达到装饰器不修改原函数的目的
#         def c_func():
#             if sex == 'man':
#                 print('你是个男的')
#             return func()
#         return c_func
#     return b_func
#
#
# @a_func(sex = 'man')
# def num():
#     print('装饰器参数带参')
#
# num()
# print(num.__name__)    #c_func
# 相当于 num = afunc(sax='man')(now)

# ----------------------------------------------------------------------------------------------------------------------
# 被装饰的函数带参数

# def q_func(func):
#     def w_func(a,b):        #a,b被装饰函数的参数
#         a += 1
#         b += 2
#         return func(a,b)
#     return w_func
#
# @q_func
# def san(a,b):
#     print(a+b)
# san(1,2)

# -----------------------------------------------------------------------------------------------------------------------------------
# __call__实例方法
# 使类实例对象变成可调用对象，可以向普通函数一样调用
# 凡是自身+()可以被调用的函数都是可调用函数
# 对于可调用对象，实际上“名称()”可以理解为是“名称.__call__()”的简写
# 可调用函数才会有__call__方法，可用于hasattr比较是否是实例属性还是实例方法


# class change:
#     def __call__(self,a,b):
#         print('请输出：',a,b)
#
# ch = Change()
#
# ch('快乐','幸福')
# ch.__call__('快乐','幸福')
# 上面两个示例等价
# -----------------------------------------------------------------------------------------------------------------------------------
# __repr__
# 通常如果我们定义了实例化对象后，会直接输出这个对象，一般显示的是：'类名+object+内存信息' ，如果我们想自定义输出信息，重写__repr__方法
# 每个类都会有__repr__方法，他们继承于object类
# 建议：类里至少写一个__repr__

# __str__
# 如果没有添加__str__方法，python会默认去寻找__repr__方法进行输出
# __str__是面向用户的，__repr__是面向程序员的
# __str__旨在提供一个友好的显示
# 功能都是实现类到字符串的转化

# a = 1
# print(a)
# print(a.__repr__())
#
# # 上面两个print等价
#
# class Dec(object):
#     def __init__(self):
#         self.name = '平平淡淡'
#         self.age = '5'
#
#     def __repr__(self):
#         return '这位同学是'+ self.name +',年纪是'+self.age
#
#     def __str__(self):
#         return '稀松平常'
#
# ds = Dec()
# print(ds)
# -----------------------------------------------------------------------------------------------------------------------------------

# __del__
# 其 作用用来销毁实例化对象
#

# class Tom(object):
#     def __init__(self):
#         '''
#         this is easy class
#         '''
#         print('实例化对象')
#     def __del__(self):
#         print('销毁实例化对象')
#
#
# took = Tom()
# cl = took
# del took
# print('******************')
# del cl
# print('----------------')

# python有自己的垃圾回收机制，在执行到del时，他不会立刻去销毁实例化对象，他使用的是自动引用计数的方式来操作，在创建实例时，会为这个
# 实例添加一个计数属性并置为0，如果有变量引用时（cl = mm），会将计数+1，并会再取消对实例化对象引用时，会将计数-1
# 直至如果计数为0时，python会认为程序不需要他，然后才会调用__del__进行删除



# -----------------------------------------------------------------------------------------------------------------------------------
# 计算函数运行时间
# import timeit
# import time
# def outtm(i):
#     time.sleep(i)
#     print(i)
#
# runtime = timeit.timeit(lambda :outtm(1),number=5)
# print(runtime)

# number  表示运行函数的次数
# -----------------------------------------------------------------------------------------------------------------------------------
# 线程中的通讯机制，多个线程可以等待某个事件执行后，在一起激活多个线程
# event
# import time
# import threading
#
#
# class MyThread(threading.Thread):
#     def __init__(self, name, event):
#         super().__init__()
#         self.name = name
#         self.event = event
#
#     def run(self):
#         print('Thread: {} start at {}'.format(self.name, time.ctime(time.time())))
#         # 等待event.set()后，才能往下执行
#         self.event.wait()
#         print('Thread: {} finish at {}'.format(self.name, time.ctime(time.time())))
#
#
# threads = []
# event = threading.Event()
#
# # 定义五个线程
# [threads.append(MyThread(str(i), event)) for i in range(1,5)]
#
# # 重置event，使得event.wait()起到阻塞作用
# event.clear()
# print(threads)
# # 启动所有线程
# [t.start() for t in threads]
#
# print('等待5s...')
# time.sleep(5)
#
# print('唤醒所有线程...')
# event.set()


# -----------------------------------------------------------------------------------------------------------------------------------

# Condition()

import threading, time

class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)  #确保先运行Seeker中的方法
        self.cond.acquire()

        print(self.name + ': 我已经把眼睛蒙上了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我找到你了哦 ~_~')
        self.cond.notify()

        self.cond.release()
        print(self.name + ': 我赢了')

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print(self.name + ': 我已经藏好了，你快来找我吧')
        self.cond.notify()
        self.cond.wait()
        self.cond.release()
        print(self.name + ': 被你找到了，哎~~~')

cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()
