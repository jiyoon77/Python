N=int(input())
arr = []
for _ in range(N):
    age, name = input().split()
    arr.append([int(age),name])

for i in sorted(arr,key=lambda x : x[0]):
    print(i[0],i[1])