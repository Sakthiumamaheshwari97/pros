luv=int(input())
heart=[]
for p in range(luv):
  heart.append(input())
mah=[]
for p in zip(*heart):
  if(p.count(p[0])==len(p)):
     mah.append(p[0])
  else:
    break
print(''.join(mah))

    
  
