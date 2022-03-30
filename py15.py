sum=0
for t in range(20):
    w=float(input('please enter value :  '))
    sum+=w
    if(t==0):
        
        min=w
        max=w
    else:
        if(w<min):
            min=w
            
avg=sum/20
print('min is=   ',min,'max is =   ',max, 'avg is =  ',avg)
input()