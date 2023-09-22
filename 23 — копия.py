a=[0]*100
a[1]=1
for i in range(1,16):
    if i+1<=16: a[i+1]+=a[i+1]
    if i*2<=16: a[i*2]+=a[i*2]
for x in range(0,101):
    if a[x]!=0:
        print(a[x])
    
