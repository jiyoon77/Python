a, b = map(list, input().split())
a.reverse()
b.reverse()
 
if int("".join(a)) > int("".join(b)):
    print("".join(a))
else:
    print("".join(b))
