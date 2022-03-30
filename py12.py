def bmm(x , y):
    if (x==0):
        return y
    return bmm(x , y % x)
x=int(input('please enter a nimber :  '))
y=int(input('please enter another number :  '))
print('bmm=  ', bmm(x , y))
input()