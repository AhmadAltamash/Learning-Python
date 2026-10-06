def var():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    print(fname + " " + lname)
    age = int(input("Enter your age: "))
    if fname == "Altamash" and age >= 18:
        print("You are Welcome")
    else:
        print("Simon Go Back")
var()
        
