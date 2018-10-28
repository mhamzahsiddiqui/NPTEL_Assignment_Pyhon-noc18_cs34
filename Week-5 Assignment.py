a,b,c=[0],[0],[0]
co,s,t=0,0,0
e=[]
d={'A':10,'AB':9,'B':8,'BC':7,'C':6,'CD':5,'D':4}
while(a[len(a)-1]!=['Students']):
    a.append(input().split('~'))
while(b[len(b)-1]!=['Grades']):
    b.append(input().split('~'))
b=b[1:-1]
while(c[len(c)-1]!=['EndOfInput']):
    c.append(input().split('~'))
c=c[1:-1]
for i in b:
    for j in c:
        if i[0] in j:
            s=s+d[j[4]]
            t+=1
    try:
        s=s/t
    except: pass
    b[co].append(str(round(s,2)))
    co+=1
    s=0
    t=0
b.sort()
for i in b:
  print('~'.join(i))
