A=list()
for _ in range(9):
    i = int(input())
    A.append(i)
    
print(max(A))
print(A.index(max(A))+1)