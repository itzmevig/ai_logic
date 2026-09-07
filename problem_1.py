n=int(input())

times=[]
o=[]
for i in range(n):
  a=list(map(int,input().split()))
  a.sort()
  times.append(a)
for i in range(n-1):
  if times[i][0]>times[i+1][0]:
    temp=times[i]
    times[i]=times[i+1]
    times[i+1]=temp
for i in range(n-1):
  if times[i][1]>times[i+1][0] and times[i+1][1]>times[i][1]:
    a=[]
    a.append(times[i][0])
    a.append(times[i+1][1])
    o.append(a)
  else:
    a=[]
    a.append(times[i][0])
    a.append(times[i][1])
    o.append(a)
print(o)