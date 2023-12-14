# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 16:04:19
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 16:04:41
def find_last_occurance(s,w):
  last_occurace=s.rfind(w)
  return last_occurace

print(find_last_occurance('lalalalla','a'))