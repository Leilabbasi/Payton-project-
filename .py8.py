value1=int(input('please enter value1 : '))
value2=int(input('please enter value2 : '))
value3=int(input('please enter value3 : '))
value4=int(input('please enter value4 : '))
value5=int(input('please enter value5 : '))
way1= ('DUPLICATE')
way2= ('ALL UNIQU')
if value1 == value2 or value1 == value3 or value1 == value4 or value1 == value5 or value2 == value3 or value2 == value4 or value2 == value5 or value3 == value4 or value3 == value5 or value4 == value5 :
    print(way1)
else:
    print(way2)