p=int(input())
q=0
while(p>0):
  d=p%10
  q=q+(d*d)
  p=p//10
print(q)
