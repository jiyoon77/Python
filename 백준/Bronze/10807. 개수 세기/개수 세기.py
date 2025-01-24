n = int(input())  
a = list(map(int, input().split())) 
k = int(input())  

num = 0
for i in range(len(a)):
    if a[i] == k:
        num += 1

print(num)  