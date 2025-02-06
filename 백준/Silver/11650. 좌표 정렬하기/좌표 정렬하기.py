import sys

n=int(sys.stdin.readline())
array=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    array.append([a, b])
array.sort()
for i in array:
    print(i[0], i[1])