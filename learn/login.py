#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,getpass

count = 0
while count < 3: #输错3次跳出
    username = input('user: ')

    forbidden = open('forbidden','r+')
    lock_list = forbidden.readlines()
    
    for lock in lock_list:
        lock_user = lock.strip('\n')        
        if username == lock_user:
            print ('user: %s had been locked !' % username)
            sys.exit(1)

    a = open('list','r')
    user_list = a.readlines()
    for i in user_list:
        (user,passwd) = i.strip('\n').split()
        if username == user:
            j = 0 
            while j <3:
                password = getpass.getpass('password: ')
                if passwd == password:
                    print ('welcome login !!!')
                    sys.exit(0)
                else:
                    print ('wrong password')
                    j += 1
            else: 
                print ('only 3 chances,user: %s locked !' % username)
                f = open('forbidden','a')
                f.write(username)
                f.write('\n')
                f.close()
                sys.exit(0)
        else:
            pass        
    count += 1     
else:
    print ('user is not exist')
