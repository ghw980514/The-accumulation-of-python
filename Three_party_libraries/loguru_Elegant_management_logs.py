'''
title: loguru
description:优雅简单的进行日志管理
import: from loguru import logger
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : pip install loguru
'''
import sys
import time
# sys.stdout.write('hello'+'\n')  ==  print 'hello'
# 官方文档：https://loguru.readthedocs.io/en/stable/overview.html#x-faster-than-built-in-logging

from loguru import logger

logger.error("That's it, beautiful and simple logging!")
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
# return:
#     2020-11-19 14:49:06.550 | DEBUG    | __main__:<module>:13 - That's it, beautiful and simple logging!
#        时间|日志级别|模块名（即哪个类中）：行号 - 日志信息
# logger是调度日志消息构造程序的接口，并且有且只有这么一个对象
#  ---------------------------------------------------------------------------------------------------------------------
# 输出到文件中
# logger.add('D:/runtime.log')     #添加日志文件存储路径


# def add(
#     self,
#     sink,      可以传入一个 file 对象，例如 sys.stderr 或者 open('file.log', 'w') 都可以,可以直接传入一个 str 字符串或者 pathlib.Path 对象，其实就是代表文件路径的，如果识别到是这种类型，它会自动创建对应路径的日志文件并将日志输出进去。
#     *,
#     level=_defaults.LOGURU_LEVEL,                        设置写入日志文件的日志级别，debug < info< warning< error< critical,设置级别越高，输出越少，如果设置info，那抹可以写入的日志信息只有info，warning，error，critical这四种
#     format=_defaults.LOGURU_FORMAT,                      用于控制日志信息的最终输出格式，，time为时间，level为级别  format="{time} {level} {message}"，写入到文件中的格式为：2020-11-19T16:43:50.357000+0800 CRITICAL this is amaz logging，，更多参数从看官方文档
#     filter=_defaults.LOGURU_FILTER,
#     enqueue=_defaults.LOGURU_ENQUEUE,                    可以配置在多进程同时往日志文件写日志的时候使用队列达到异步功效
#     retention=' 1 week'                                  配置日志的最长保存时间，可用于清除时间太久已经没有意义的日志   Examples: "1 week, 3 days", "2 months"
#     rotation="500 MB"                                    配置日志文件的最大磁盘占有数，设置后如果日志文件达到500mb，那抹就会创建一个新的日志文件，，需要把日志文件名设置成动态形式
#     compression='zip'                                    设置日志文件的压缩格式，可选格式为"gz", "bz2", "xz", "lzma", "tar", "tar.gz", "tar.bz2","tar.xz", "zip"
#     **kwargs
# )

# format
# logger.remove()                                         会将addid的的任务删除掉，，不会继续下面的日志存储，可以实现日志的刷新重新写入操作


td = logger.add('D:/runtime.log', format="<green>{time}</green> {level} {message} ,{module}",level="DEBUG",enqueue=True,retention=' 1 week',rotation="500 MB",compression='zip')
logger.debug('this is cool logging')
logger.info('this is amaz logging')
logger.warning('this is amaz logging')
logger.error('this is amaz logging')
logger.remove(td)
logger.critical('this is amaz logging')
