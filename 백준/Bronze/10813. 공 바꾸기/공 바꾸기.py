N, M = map(int, input().split())
B = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    B[i-1], B[j-1] = B[j-1], B[i-1]

for B in B:
    print(B, end=' ')