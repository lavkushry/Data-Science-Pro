def count_occurance(s,w):
  count=0
  for i in s:
    if i==w:
      count=count+1
  return count

print(count_occurance('lalalalalla','l'))