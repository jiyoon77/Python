from collections import Counter

num = int(input())
Scard = list(map(int, input().split()))
fnum = int(input())
Fcard = list(map(int, input().split()))

Scard_count = Counter(Scard)

finalNum = [Scard_count[i] for i in Fcard]

print(*finalNum)
