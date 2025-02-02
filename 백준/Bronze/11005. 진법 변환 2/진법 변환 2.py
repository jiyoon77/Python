num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N,B=map(int,input().split())
A=''

while N:
    A=num[N%B]+A
    N//=B

print(A)