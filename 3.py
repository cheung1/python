#!/usr/bin/python
#encoding=utf-8

import time

#1.提示用户输入信息
name = raw_input('请输入姓名:')
QQ = raw_input('请输入QQ:')
tel = raw_input('请输入手机号:')

#模拟打印的过程

print'系统正在打印中...3'
time.sleep(1)
print'系统正在打印中...2'
time.sleep(1)
print'系统正在打印中...1'
time.sleep(1)

#2.从相应的变量中取出数据，然后打印
print'======================'
print('姓名:%s'%name)
print('QQ:%s'%QQ)
print('手机号:%s'%tel)
print'======================'

