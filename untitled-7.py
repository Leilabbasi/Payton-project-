#17
def print_big_enough():
    a=2
    lst=[1,2,3,4,5,6]
    for i in lst :
        if i>=a :
            print(i)
            
            
    return i
    
print(print_big_enough())
#________________________________

#20
m = [[1 for i in range(9)] for j in range(6)]
for i in range(6):
    for j in range(9):
        print(m[i][j], end='  ')
        print('\n')
        print('\n\n')
        m[2][4] = 0

for i in range(6):
    for j in range(9):
        print(m[i][j], end='  ')
        print('\n')