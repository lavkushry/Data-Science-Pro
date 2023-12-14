# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 21:17:18
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 21:18:28
def shortest_word_in_the_string(s):
  str=list(s.split())
  shortest_word = min(str, key=len)
  return shortest_word

print(shortest_word_in_the_string("hello world, welcome to python programming."))