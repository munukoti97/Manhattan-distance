a=(raw_input('enter the 1 string:'))
d=(raw_input('enter the 1 string:'))
b=a.split(",")
e=d.split(",")
c=[]
le=len(b)
le1=len(e)

i=0
r=0
u=0
d=0
l=0
s=b[0]

sum=0
sum1=0
l=0
r=0
d=0
u=0
while (i<le):
    s=b[i]
    if s[0:1]=='U':
        v=int(s[1:])
        sum1=sum1+v
        if u<sum1:
            u=sum1
    if s[0:1]=='D':
        v=int(s[1:])
        sum1=sum1-v
        if sum1<0:
            v=abs(sum1)
            if d<v:
                d=v
    if s[0:1]=='L':
        v=int(s[1:])
        sum=sum-v
        if sum<0:
            v=abs(sum)
            if l<v:
                l=v
    if s[0:1]=="R":
        v=int(s[1:])
        sum=sum+v
        if r<sum:
            r=sum
        
        
    i=i+1
i=0

sum=0
sum1=0
l1=0
r1=0
u1=0
d1=0


while (i<le1):
    s=e[i]
    if s[0:1]=='U':
        v=int(s[1:])
        sum1=sum1+v
        if u1<sum1:
            u1=sum1
    if s[0:1]=='D':
        v=int(s[1:])
        sum1=sum1-v
        if sum1<0:
            v=abs(sum1)
            if d1<v:
                d1=v
    if s[0:1]=='L':
        v=int(s[1:])
        sum=sum-v
        
        if sum<0:
            v=abs(sum)
            if l1<v:
                l1=v
    if s[0:1]=="R":
        v=int(s[1:])
        sum=sum+v
        if r1<sum:
            r1=sum
    i=i+1



f=[]
i=0
if r1>r:
    r=r1
if u1>u:
    u=u1
if l1>l:
    l=l1
if d1>d:
    d=d1
ro=u+d+5
co=l+r+5

while i<ro:
    f.append([])
    for j in range(0,co):
        f[i].append(0)
    i=i+1
h=u+2
k=l+2

i=0 
h1=h
k1=k
while (i<le):
    
    s=b[i]
    if s[0:1]=='U':
        v=int(s[1:])
        j=h1-1
        while j>=(h1-v):
            f[j][k1]=1 
            j=j-1
        h1=h1-v
    
    if s[0:1]=='D':
        v=int(s[1:])
        j=h1+1 
        while j<=(h1+v):
            f[j][k1]=1 
            j=j+1
        h1=h1+v
        
    
    if s[0:1]=='L':
        v=int(s[1:])
        j=k1-1
        while j>=(k1-v):
            f[h1][j]=1 
            j=j-1 
        k1=k1-v
        
    if s[0:1]=="R":
        v=int(s[1:])
        j=k1+1
        while j<=(k1+v):
            f[h1][j]=1 
            j=j+1 
        k1=k1+v 
    i=i+1
        
i=0 

h1=h
k1=k
min=30000

while (i<le1):
    
    s=e[i]
    if s[0:1]=='U':
        v=int(s[1:])
        j=h1-1
        while j>=(h1-v):
            if f[j][k1]==1:
                dis=abs(h-j)+abs(k-k1)
                if min>dis:
                    min=dis
            else:
                f[j][k1]=1 
            j=j-1
        h1=h1-v
    
    if s[0:1]=='D':
        v=int(s[1:])
        j=h1+1 
        while j<=(h1+v):
            if f[j][k1]==1:
                dis=abs(h-j)+abs(k-k1)
                if min>dis:
                    min=dis
            else:
                f[j][k1]=1  
            j=j+1
        h1=h1+v
        
    
    if s[0:1]=='L':
        v=int(s[1:])
        j=k1-1
        while j>=(k1-v):
            if f[h1][j]==1:
                dis=abs(h-h1)+abs(k-j)
                if min>dis:
                    min=dis
            else:
                f[h1][j]=1
            j=j-1 
        k1=k1-v
        
    if s[0:1]=="R":
        v=int(s[1:])
        j=k1+1
        while j<=(k1+v):
            if f[h1][j]==1:
                dis=abs(h-h1)+abs(k-j)
                if min>dis:
                    min=dis
            else:
                f[h1][j]=1 
            j=j+1 
        k1=k1+v 
                
        
        
    i=i+1
i=0 

print(min)










