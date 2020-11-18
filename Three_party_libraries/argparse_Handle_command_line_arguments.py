'''
title: argparse
description: argparse是python标准库里面用来处理命令行参数的库,当你的代码需要频繁的切换参数时，就可以使用此模块
import: import argparse
auther: xiaoguo
python version: 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
installation : python标准库自带
'''
# 命令行参数包括位置参数和选项参数
# 位置参数：cd  d:/      程序根据该参数的位置来确定
# 选线参数：ls -l    -l就是选项参数，是应用程序自己定义好的参数，不能随意更改指定


# 基本操作
# import argparse
# parser = argparse.ArgumentParser(description='这是个神奇的程序',epilog='见证奇迹的时刻')       #创建一个解析对象
# # parser.add_argument('echo')                 #向该对象添加要关注的命令行参数和选项
# parser.add_argument('echo',help='echo the string use here',type=int)                 #向该对象添加要关注的命令行参数和选项
# asse = parser.parse_args()                    #开始解析
# print(asse)
# print(asse.echo)
# print(asse.echo**3)

# return:
    # D:\accumulation_python\Three_party_libraries>python3 argparse_Handle_command_line_arguments.py 4
    # Namespace(echo=4)
    # 4
    #64

# 各方法参数和使用  ArgumentParser()
# prog = None - 程序名
# 一般我们只使用description
# description = None, - help时显示的开始文字        在命令行执行   python3 py文件名 -h  时显示
# epilog = None, - help时显示的结尾文字
# parents = [], -若与其他参数的一些内容一样，可以继承
# formatter_class = argparse.HelpFormatter, - 自定义帮助信息的格式
# prefix_chars = '-', - 命令的前缀，默认是‘-’
# fromfile_prefix_chars = None, - 命令行参数从文件中读取
# argument_default = None, - 设置一个全局的选项缺省值，一般每个选项单独设置
# conflict_handler = 'error', - 定义两个add_argument中添加的选项名字发生冲突时怎么处理，默认处理是抛出异常
# add_help = True - 是否增加 - h / --help选项，默认是True)




# add_argument()
# type    规定传入的选项类型,默认为字符串类型，例：type=int
# action
# default：没有设置值情况下的默认参数
# required: 表示这个参数是否一定需要设置 如果设置了required=True,则在实际运行的时候不设置该参数将报错,如'--verberition'
# choices：参数值只能从几个选项里面选择     例：choices=['alexnet', 'vgg']  参数只能从这两个中选一个，填别的会报错
# help：指定参数的说明信息     ，有时候执行者，不知道参数是什么含义，可以在这里表明
# nargs： 设置参数在使用可以提供的个数    例：.add_argument('-name', required=True, nargs='+')
    # 值  含义
    # N   参数的绝对个数（例如：3）
    # '?'   0或1个参数
    # '*'   0或所有参数
    # '+'   所有，并且至少一个参数
# dest：设置参数在代码中的变量名，argparse默认的变量名是--或-后面的字符串，但是你也可以通过dest=xxx来设置参数的变量名，然后在代码中用args.xxx来获取参数的值。

# 传入可选参数
import argparse
parserone = argparse.ArgumentParser()
parserone.add_argument('--verberition',help='verberition  ouput')
assee = parserone.parse_args()
if assee.verberition:
    print('verberition retu,on')


# 使用--verberition时（这个值可以随意指定）必须指定一个值，可以是任何值，不指定值会报错