#!/usr/bin/env python
# -*- coding: utf-8 -*-

budget = int(input('input your budget: '))
money = 0 

while 1:

    list = '''
    Welcome  to  Alex’s  shopping  mall,  below  are  the  things  we  are  selling: 
    1. MacBook  Air       7999 
    2. Starbucks  Coffee    33 
    3. Iphone  6Plus      6188 
    4. Iphone 7p	  7288 
    '''
    print (list)
    list = ('MacBook Air','7999','Starbucks Coffee','33','Iphone 6Plus','6188','Iphone 7p','7288')
    p1 = int(list[1])
    p2 = int(list[3])
    p3 = int(list[5])
    p4 = int(list[7])
    #print (list[0:3])

    basket = input('choose the No. you want: ')
    if basket == 'q':
        break
   
    if budget > p1+p2+p3+p4:
        print ('over budget\n')



print ('所选商品，剩余金额：')

