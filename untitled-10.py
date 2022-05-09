#19
def reverse():
    lst=[1,2,3,4,5,6,7,8,9]
    lst.reverse()
    print(lst)
    
print(reverse())
#_________________________________________
#23
def check_winner(m):
    new_mat = [[0] * len(m)] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_mat[j][i] = m[i][j]
    for i in m:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    for i in new_mat:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    if m[0][0] == m[1][1] == m[2][2] == 'X':
        return 'X'
    elif m[0][0] == m[1][1] == m[2][2] == 'O':
        return 'O'
    if m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'X'
    elif m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'O'
    return ' '