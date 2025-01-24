str = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in str:
        print(str.index(i))
    else:
        print(-1)