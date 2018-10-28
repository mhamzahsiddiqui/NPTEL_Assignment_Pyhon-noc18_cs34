def intreverse(n):
  s=0    
  while(n>0):
    d=n%10    
    s=s*10+d   
    n=n//10    
  return(s)   


def matched(a):
  if a.index('(')>a.index(')'): return False
  elif a.count('(')==a.count(')'): return True
  else: return False
        


  
def sumprimes(l):
    sum=0
    for i in range(0,len(l)):
        fl=[]
        d=l[i]
        for j in range(1,d+1):
            if d%j==0:
                fl=fl+[d]
        if len(fl)==2:
            sum=sum+d
    return(sum)  
