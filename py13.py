def number_len(M):
    d=0
    while(M!=0):
        M//=10
        d+=1
        return d
def power_digits(M,K):
    A=0
    while(M!=0):
        U=M % 10
        A+=U**K
        M//=10
    return A

for X in range(1,10000,1):
    l= number_len(X)
    A=power_digits(X,l)
    if(A==X):
        print(A,end=' , ')
input()