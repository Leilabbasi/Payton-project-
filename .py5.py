i=int(input('please enter number i: ')) 
j=int(input('please enter number j: '))
k=int(input('please enter number k: '))
if i<j :
    if j<k :
        i=j
    else :
        j=k
else :
    if j>k :
        j=i
    else :
        i=k
print("i =" ,i, "j =",j , "k =",k )
#i is 3, j is 5, and k is 7 => i=5 , j=5 , k=7
#i is 3, j is 7, and k is 5 => i=3 , j=5 , k=5
#i is 5, j is 3, and k is 7 => i=7 , j=3 , k=7
#i is 5, j is 7, and k is 3 => i=5 , j=3 , k=3
#i is 7, j is 3, and k is 5 => i=5 , j=3 , k=5 
#i is 7, j is 5, and k is 3 => i=7 , j=7 , k=3
