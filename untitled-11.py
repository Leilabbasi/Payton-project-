#18

    
def next_number():
        lst=[1,3,5,6]
        m=0
        for i in lst:
                if i> m:
                        m=i
            
            
        for i in range(1,m+1):
                if i not in lst:
                        return i
        print(i)
    
print(next_number())
#______________________________________________


#22
                
def Q22(m):
        new_mat = [[0] * len(m)] * len(m)
        for i in range(len(m)):
                for j in range(len(m[0])):
                        new_mat[j][i] = m[i][j]
        flag = 0
        for i in range(len(m)):
                for j in range(len(m)):
                        if m[i] == new_mat[j]:
                                flag = 1
        if flag:
                return True
        else:
                return False
