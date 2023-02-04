def switch():
    a=int(input("enter first number: "))
    b=int(input("Enter second number:"))
    
    
    print("Press 1 for addition:\npress 2 for substruction:\npress 3 for multiplication:\npress 4 for divition:\n")
    option=int(input("enter your choice:"))
    
    def addition():
        result=a+b
        print("Your result is={}".format(result))
    def substruction():
        result=a-b
        print("Your result is={}".format(result))
    def multiplication():
        result=a*b
        print("Your result is={}".format(result))
    def divition():
        result=a/b
        print("Your result is={}".format(result))
    def default():
        print("incorrect option:")
        
    dict={1:addition,2:substruction,3:multiplication,4:divition}
    
    dict.get(option,default)()
    
switch()
