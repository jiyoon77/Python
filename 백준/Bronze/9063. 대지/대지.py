n = int(input())
A, B = [], []
for _ in range(n):
    x, y = map(int, input().split())
    A.append(x)
    B.append(y)
print((max(A) - min(A)) * (max(B) - min(B)))