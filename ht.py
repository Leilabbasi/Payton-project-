def hanoi(n , A , B , C):
    if n==1:
        print('move disk' , n , 'from', A , 'to' , C)
    else:
        hanoi(n-1, A, C , B )
        print('move disk' , n , 'from' , A , 'to' , C ,)
        hanoi(n-1, B , A , C)



n=int(input('pls enter a number of n : '))
hanoi(n , 'A','B','C')