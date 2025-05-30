n = int(input().strip())
copy = 10 ** len(str(n))
count = 0

while n * 2 < copy:
    n *= 2
    count += 1
print(count)