#!/usr/bin/python
#-*- encoding=utf-8
import time
#减法运算

a = raw_input('请输入减数:')
b = raw_input('请输入被减数：')
c = int(a)-int(b)

print '系统正在计算中...3'
time.sleep(1)
print '系统正在计算中...2'
time.sleep(1)
print '系统正在计算中...1'
time.sleep(1)

print '========================='
print('相减结果为:   %d'%c)
print '========================='
