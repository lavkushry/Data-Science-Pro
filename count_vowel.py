# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 14:06:19
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 14:11:04
def count_vowel(s):
  s_lower=s.lower()
  count=0
  vowels='aeiou'
  for i in s_lower:
    if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u' ):
      count=count+1
  return count

print(count_vowel('aeiou'))