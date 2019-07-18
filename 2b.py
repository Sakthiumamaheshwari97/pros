from itertools import combinations
oj,i=map(int,input().split())
u=len(str(oj))
r=list(combinations(str(oj),u-i))
r=sorted(r)
print("".join(r[0]))
