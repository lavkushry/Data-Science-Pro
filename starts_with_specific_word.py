# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 20:35:40
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 20:36:46
#Check if a string starts with a specific word or phrase.

def starts_with_specific_word(s,w):
  return s.startswith(w)

print(starts_with_specific_word('Hello world, welcome to the universe','Hello'))