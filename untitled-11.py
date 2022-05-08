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
                
        
        
    
    
    
