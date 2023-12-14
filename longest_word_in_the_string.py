# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 21:09:41
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 21:15:14
#Find the longest word in a string.
def longest_word_in_the_string(s):
  str=list(s.split())
  longest_word = max(str, key=len)
  return longest_word

print(longest_word_in_the_string("hello world, welcome to python programming."))