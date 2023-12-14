# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 21:34:12
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 21:46:01
#Reverse the order of words in a string.

def reverse_order_of_words_(s):
  words=s.split()
  words.reverse()
  return ' '.join(words)
  

print(reverse_order_of_words_("This is a sample string"))