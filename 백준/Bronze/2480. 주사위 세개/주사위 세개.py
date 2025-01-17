A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + (A * 1000))
elif A == B or A == C:
    print(1000 + (A * 100))
elif B == C:
    print(1000 + (B * 100))
else:
    max_val = max(A, B, C)
    print(max_val * 100)