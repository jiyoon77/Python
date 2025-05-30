Tnum = int(input()) 
for i in range(Tnum): # 총 2번
    n = int(input()) # 단어 수
    pubKeyFirst = input().split(" ") 
    PubKeySecond = input().split(" ") 
    Crypto = input().split(" ")

    ListFirst = []
    for i in pubKeyFirst:
        ListFirst.append(PubKeySecond.index(i))
 
    result = []
    for i in ListFirst:
      result.append(Crypto[i])
    print(*result)