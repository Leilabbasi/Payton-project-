def func(X):
    return X**3-X**2+2

def derivfunc(X):
    return 3*X**2-2*X

def newtonraphson(X):
    b= func(X)/derivfunc(X)
    
    for s in range(10):
        b=finc(X) / derivfinc(X)
        
        '''''''X(e+1)=X(e)-f(X)/f'(X)
        X=X-b
        print('the numbers root that you have entered is : ','%.4f'%X)
        
        X0=-20
        newtonraphson(X0)
        input()
        