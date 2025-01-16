A = int(input())
B = int(input())

OneB= int(B%10)
TwoB= int((B//10)%10)
ThreeB= int(B//100)

print(A * OneB)
print(A * TwoB)
print(A * ThreeB)

a=int(A * OneB)
b=int(A * TwoB)
c=int(A * ThreeB)

print(a+ b*10 + c*100)