n,m = map(int, input().split())
B = [i for i in range(1,n+1)]
temp = 0
for k in range(m):
  i,j = map(int, input().split())
  temp = B[i-1:j]
  temp.reverse()
  B[i-1:j] = temp

for k in range(n):
  print(B[k])