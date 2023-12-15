#To chheck the eligibilty to drive and check whether the person's name is in tghe registered list
Lst=["Niya","Sonu" ]
a=int(input("enter your age: "))
if a>=18:
    name=input("Enter your name:")
    if name in Lst:
         print ('you are in the registered list')
    else:
         print("you are not in the registered list")
else:
    print("you are not eligible for driving")