N=int(input())
stu=[]

for i in range(N):
    stu.append(input().split())

stu.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in stu:
    print(i[0])