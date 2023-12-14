# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 20:39:43
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 20:39:58
#Check if a string ends with a specific word or phrase.

def ends_with_specific_word(s,w):
  return s.endswith(w)

print(ends_with_specific_word('Hello world, welcome to the universe','universe'))