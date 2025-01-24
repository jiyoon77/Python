import sys
input = sys.stdin.readline

N = int(input().strip())
score = list(map(int, input().split()))
max_score = max(score)
for i in range(N):
    score[i] = score[i] / max_score * 100
print(sum(score) / N)