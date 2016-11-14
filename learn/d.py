#!/usr/bin/env python
# -*- coding: utf-8 -*-


#def printme( str ):
#   "打印任何传入的字符串"
#   print str;
#   return;
 
#printme( str = "My string");
                 
#def sum( arg1, arg2 ):
#   total = arg1 + arg2; # total在这里是局部变量.
#   print "函数内是局部变量 : ", total
#   #return total;
# 
#print sum( 10, 20 );


#Money = 2000
#def AddMoney():
#   # 想改正代码就取消以下注释:
#    global Money
#    Money = Money + 1
#     
#print Money
#AddMoney()
#print Money


#import math 
#import os
#content = dir(math)
#content1 = dir(os)
#print content,content1
#

#
#o = open("/foo.txt","wb")
#o.write( "www.baidu.com........")

import os 

#os.rename("foo.txt","asdasdasd")
#os.remove("asdasdasd")
os.chdir('/home/test/testos')
os.mkdir("hahaha")
print os.getcwd()
