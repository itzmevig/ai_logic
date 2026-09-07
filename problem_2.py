n=int(input())
a=list(map(int,input().split()))
m=int(input())
m_sum=0
for i in range(m-1,n):
  sp=a[i-2:i+1]
  sum=0
  for j in sp:
    sum+=j
  if sum>m_sum:
    m_sum=sum
print(m_sum)
