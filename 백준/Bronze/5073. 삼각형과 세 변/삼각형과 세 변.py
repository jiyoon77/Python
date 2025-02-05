while True:
  X = list(map(int,input().split()))
  a,b,c= sorted(X,reverse=True)
  if a==0 and b==0 and c==0:
    break
  
  elif (a <b +c)==True :
    if a==b==c:
      print('Equilateral')
    elif a==b or a==c or b==c:
      print('Isosceles')
    else:
      print('Scalene')
  else:
    print("Invalid" )