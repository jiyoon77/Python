count = 0

for i in range(int(input())):
    a = input()

    if list(a) == sorted(a, key=a.find):
        count += 1
print(count)
