'''
title: argparse
description: argparse是python标准库里面用来处理命令行参数的库
import: import argparse
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : python标准库自带
'''
# 命令行参数包括位置参数和选项参数
# 位置参数：cd  d:/      程序根据该参数的位置来确定
# 选线参数：ls -l    -l就是选项参数，是应用程序自己定义好的参数，不能随意更改指定


# 基本操作
import argparse
parser = argparse.ArgumentParser()       #创建一个解析对象
parser.add_argument()                 #向该对象添加要关注的命令行参数和选项
parser.parse_args()                    #开始解析


# 各方法参数和使用

