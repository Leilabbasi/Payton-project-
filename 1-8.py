#1
#we can't change tpl but in lst this is possible

#2
#these aren't deiffrent and [] do same thing in lst and tpl

#3
#the tuple is immuutable

#4
#the elements in tpl are orderd

#5
tpl=(1,2,3,4,5,6,7,8)
print(tpl[-6:-2])

#6
tpl=(1,2,3,4,5,6,7,8)
print(tpl[-5:-1])

#7
tpl=(7, 10, -3, 18, 6, 10)
tpl2=('x',)
tpl3=('y',)

tpl4=tpl2+tpl+tpl3 
print(tpl4)


#8
def product():
    tpl=(2.0,3.5,4.0)
    for i in tpl:
        
        if tpl is ():
            return 1
        else :
            product=tpl[0]*tpl[1]*tpl[2]
            return product
print(product())