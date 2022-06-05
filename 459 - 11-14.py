#11
lst = [0, 0, 0, 0]
try :
        with open('data.txt', 'r') as f:
                count = 0
        for line in f.readlines():
                lst[count] = int(line)
                count += 1
except IndentationError:
        print("IndentationError")






#12
#a output when user enters 22:
#Begin
#22
#22
#End

#output when user enters ZZ :
#Begin
#zz
Traceback ('most recent call last')
File in [module]
x = int(input())
ValueError: invalid literal for int() with base 10: 'zz'

#b output when user enters 22:
#Begin
#22
#22

#output when user enters ZZ :
#Begin
#zz
#Wrong!
#End

#coutput when user enters 22:
#Begin
#22
#22

#output when user enters ZZ :
#Begin
#ZZ
Traceback (most recent call last):
        File in [module]
        x = int(input())
ValueError: invalid literal for int() with base 10: 'ZZ'


#d output when user enters 22:
#Begin
#22
#22

#output when user enters ZZ :
#Begin
#ZZ
#Wrong!
#End

#e output when user enters 22:
#Begin
#22
#22
#Wow
#End

#output when user enters ZZ :
#Begin
#ZZ
#Wrong!


#f output when user enters 22:
#Begin
#22
#22
#Done
#End

#output when user enters ZZ :
#Begin
#ZZ 
#Wrong!
#Done
#End


#g output when user enters 22 :
#Begin
#22
#22
#Wow
#Done
#End

#output when user enters ZZ :
#Begin
#ZZ
#Wrong!
#Done
#End



#13
#should write value error before of exception error



#14
# this is has name error 