income = int(input('please enter number of income : '))
taxation = ' '
if income <1000:
    taxation =' '
if  1000<income<=2500 :
    taxation =int(income*10/100)
if 2500<income<=4000:
    taxation = int(income*15/100)
if 4000<income<=6000 :
    taxation = int( income*20/100) 
if income>=8000 :
    taxation = int(income*30 /100)
print(taxation)
        
    