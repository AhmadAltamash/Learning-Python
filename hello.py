def var():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    print(fname + " " + lname)
    age = int(input("Enter your age: "))
    if fname == "Altamash" and lname == "Ahmad" and age >= 18:
        print(fname + " " + lname + ", " + "You are Welcome")
    else:
        print(fname + " " + lname + ", " + "Simon Go Back")
var()
        
