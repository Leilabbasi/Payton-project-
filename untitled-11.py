#18
def next_number():
    lst=[1,3,4,5,7]
    sp=1
    for i in lst:
        if i==1 not in lst:
            pribt(sp)
    
print(next_number())