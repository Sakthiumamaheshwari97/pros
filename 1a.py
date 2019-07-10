def longest(shas,shes):
  if(shas in shes):
    return shas
  else:
    return longest(shas[0:len(shas)-1],shes)
ch=int(input())
che=[]
for _ in range(0,ch):
    che.append(input())
che.sort()
print(longest(che[0],che[ch-1]))
