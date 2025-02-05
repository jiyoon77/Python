A = []
B = []

for i in range(3):
    x, y = map(int, input().split())
    A.append(x)
    B.append(y)

for i in range(3):
    if A.count(A[i]) == 1:
        x = A[i]
    if B.count(B[i]) == 1:
        y = B[i]

print(x, y)