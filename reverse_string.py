# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 13:48:14
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 13:51:40
l=input("Enter the string to reverse")
m=''
for i in l[-1: :-1]:
  m=m+i

print(m)
  