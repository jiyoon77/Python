import sys
arr = []

for i in range(int(sys.stdin.readline().strip())):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))

arr.sort() 
arr.sort(key = len)

for i in arr:
    print(i)