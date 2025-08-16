def add(fristName: str | None , lastName: str = None):
    if(firstName !=None):
        firstName.capitalize()
    
    return firstName +  " " + lastName

fname = None
lname = "Gates"

name = add(fname, lname)
print(name)
