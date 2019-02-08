s=int(input())
c=list(map(int,str(s)))
d=list(map(lambda x:x**3,c))
if(sum(d)==s):
  print("yes")
else:
  print("no")
