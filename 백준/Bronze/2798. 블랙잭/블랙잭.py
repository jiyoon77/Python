N, M = map(int, input().split())
card = list(map(int, input().split()))
cardSum = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum =  card[i] + card[j] + card[k]
            if sum > M:
                continue
            else:
                cardSum.append(sum)
print(max(cardSum))