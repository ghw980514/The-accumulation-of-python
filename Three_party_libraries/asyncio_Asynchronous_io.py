'''
title: asyncio
description:异步i/o协程
import: import asyncio
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : python3.7+可用
'''

# event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
# future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
# async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
# 程序在遇到阻塞操作时，会自动先去处理其他操作，等阻塞操作完成后，在通知cpu来处理阻塞操作

import asyncio
import time

# now = lambda :time.time()     #匿名定义一个now()函数
#
# async def some_work(x):
#     print('num:',x)
# start = now()
# coroutine = some_work(2)
# loop = asyncio.get_event_loop()         #创建事件循环
# loop.run_until_complete(coroutine)      #将协程注册到事件循环，并启动事件循环
# print('time:',now() - start)

# return:
#     num: 2
#     time: 0.0009999275207519531

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# now = lambda :time.time()
#
# async def some_work(x):
#     print('num:',x)
# start = now()
# coroutine = some_work(2)
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)             #创建一个task任务对象
# print(task)
#
# loop.run_until_complete(task)
# print(task)
# print('time:',now() - start)

# return:
#     <Task pending name='Task-1' coro=<some_work() running at D:/accumulation_python/Three_party_libraries/asyncio_Asynchronous_io.py:38>>
#     num: 2
#     <Task finished name='Task-1' coro=<some_work() done, defined at D:/accumulation_python/Three_party_libraries/asyncio_Asynchronous_io.py:38> result=None>
#     time: 0.0019998550415039062

# 创建task后，task在加入事件循环之前是pending状态，因为do_some_work中没有耗时的阻塞操作，task很快就执行完毕了。后面打印的finished状态。
# asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task，run_until_complete的参数是一个futrue对象。当传入一个协程，
# 其内部会自动封装成task，task是Future的子类。isinstance(task, asyncio.Future)将会输出True。

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 回调函数
# now = lambda :time.time()
#
# async def some_work(x):
#     print('num:',x)
#     return 'Dears {}' .format(x)
#
# def callback(future):
#     print('callback:',future.result())
#
# start = now()
# coroutine = some_work(2)
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)             #创建一个task任务对象
# print(task)
# task.add_done_callback(callback)               #为task任务添加一个回调函数,coroutine执行结束时候会调用回调函数。并通过参数future获取协程执行的结果。我们创建的task和回调里的future对象，实际上是同一个对象。
# print(task)
# loop.run_until_complete(task)
# print('time:',now() - start)


# 在回调函数中我们可以使用result方法获取task的返回值
# return:
    # <Task pending name='Task-1' coro=<some_work() running at D:/accumulation_python/Three_party_libraries/asyncio_Asynchronous_io.py:65>>
    # <Task pending name='Task-1' coro=<some_work() running at D:/accumulation_python/Three_party_libraries/asyncio_Asynchronous_io.py:65> cb=[callback() at D:/accumulation_python/Three_party_libraries/asyncio_Asynchronous_io.py:69]>
    # num: 2
    # callback: Dears 2
    # time: 0.0009999275207519531


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# now = lambda: time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
#
# print('Task ret: ', task.result())
# print('TIME: ', now() - start)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 建立tcp连接
    reader, writer = await connect
    # reader用于读取连接数据
    # writer用于给服务器写信息
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 准备向服务器发送的数据
    await writer.drain()
    # 向服务器发送数据，如果数据量大，可能会造成阻塞操作
    while True:
        line = await reader.readline()
        # 接收服务器返回的数据，
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()






















