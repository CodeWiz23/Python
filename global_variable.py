x = "good"

def student():
 global x # if there is not this line x will print top x cause "x = best " traps into the function boundary
 x = "best"

student()

print("Python is the  " + x )