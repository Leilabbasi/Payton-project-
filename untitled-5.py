#15
def sum_positive():
    a=0
    lst=[-2,-1,8,3,2,-9]
    for i in lst:
        if i> 0:
            a += i
        else :
            a += 0
            
    return a
print(sum_positive())
