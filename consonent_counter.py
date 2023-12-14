# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 14:14:37
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 14:17:32
def consonent_counter(s):
  s_lower=s.lower()
  count=0
  vowels='aeiou'
  for i in s_lower:
    if (i !='a' and i!='e' and i!='i' and i !='o' and i!='u' ):
      count=count+1
      
      
  return count

print(consonent_counter("aeiou"))