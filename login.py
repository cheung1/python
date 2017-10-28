#!/usr/bin/python
#-*-encoding=utf-8
import time

name = raw_input('请输入您的登录名:')
passwd = raw_input('请输入您的密码:')

print('系统正在验证您的信息...3')
time.sleep(1)
print('系统正在验证您的信息...2')
time.sleep(1)
print('系统正在验证您的信息...1')
time.sleep(1)

if name == 'xt' and passwd == '123456':
	print('您的用户名及密码输入正确，系统正在登录..')
else:
	print('您的用户名及密码不匹配') 

