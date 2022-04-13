#simple looping calculator in python, made by JGS

print("Hello!, do you want my help in any of your calculation?")
x= input("yes/no  ")
if x == "no":
    print("thank you sir, run me whenever you need my help :)")

elif x== "yes":
    print("we will be happy to help you!")

x1 = int(input("please enter your first number here:  "))
x2 = input("please select your operator : (add,subtract,multiplicate,divide)  ")
x3 = int(input("please enter your second number here:  "))

if x2 == "add":
    print(x1+x3)
    print("Here goes your answer!")

elif x2 == "subtract":
    print(x1-x3)
    print("Here goes your answer!")

elif x2 == "divide":
    print(x1/x3)
    print("Here goes your answer!")

elif x2 == "multiply":
    print(x1*x3)
    print("Here goes your answer!")

elif x2 == " ":
    print("invalid entry")

b = print("do you want to continue? (yes/no)")

a = input("enter your ans here-  ")
if a == "no":
    print("bye")

#here begins the while loop-    

while a == "yes":
    print("Hello!, do you want my help in any of your calculation?")
    x= input("yes/no  ")
    if x == "no":
        print("thank you sir, run me whenever you need my help :)")
    elif x== "yes":
    
            print("we will be happy to help you!")
            x1 = int(input("please enter your first number here:  "))
            x2 = input("please select your operator : (add,subtract,multiplicate,divide)  ")
            x3 = int(input("please enter your second number here:  "))
            if x2 == "add":
                print(x1+x3)
                print("Here goes your answer!")
            elif x2 == "subtract":
                     print(x1-x3)
                     print("Here goes your answer!")
            elif x2 == "divide":
                         print(x1/x3)
                         print("Here goes your answer!")
            elif x2 == "multiply":
                              print(x1*x3)
                              print("Here goes your answer!")
            elif x2 == " ":
                                  print("invalid entry")
                                  print("do you want to continue? (yes/no)  ")
                                  a = input("enter your ans here-  ")
                                  print("bye")


while x == "no":
    break



    
        

    
    

    





    
    

   
    


    
    

   
    


    





    




#this loop continewis untill the user enter the string "no"
# this code was written by Johan george sajin    



