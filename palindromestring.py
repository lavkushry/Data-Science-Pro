# -*- coding: utf-8 -*-
# @Author: Roni Laukkarinen
# @Date:   2023-12-14 13:53:24
# @Last Modified by:   Roni Laukkarinen
# @Last Modified time: 2023-12-14 13:59:12
def ispalindrome(s):
  s=s.lower()
  rev_s=s[::-1]
  return s== rev_s
print(ispalindrome('Lavkush'))
