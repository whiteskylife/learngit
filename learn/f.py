#!/usr/bin/env python
# -*- coding: utf-8 -*-

#flag = 0 

#while 1:
#    username = input("user:")
#    password = input("passwd:")
#
##    if username == 'root' or password == 123: 此处123如果不加‘’‘’ 被当做赋值执行
#    if username == 'root' and password == '123':
#        print ("welcome login !!!")
#    else:
#        print ("out !!!")
#        flag += 1 
#        if flag > 2:
#            print (username,'will be locked !!!')
#            break 
#        

f = open('list','r')
a = [f.read()]
print (a[0:-1])
#f.close

username = input('user:')

if username in f:
    print ('yeah',f)
else:
    print ('xxxxxxxxxxxxxx')

#f = [open('list')]
#    print (f[0:])
