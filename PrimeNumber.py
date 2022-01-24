number = int(input("Enter any number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number, "is not prime number")
            break
    else:
            print(number, "is prime number")
            
            
            ////////////////////////////
            
            
for num in range(100,200):
    if all(num%i != 0 for i in range(2,num)):
        print(num)
