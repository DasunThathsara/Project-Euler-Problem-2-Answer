y=0
w=[0,1]
x=0
X=1
c=0
while y<4000000:
    
    for i in range(x,X):
        y=w[i]+w[i+1]
    w.append(y)
    x=x+1
    X=X+1
    if y%2==0:
        c=c+y
print(c)
