def myhelloworld():
    print("Hello World")
    
myhelloworld()

def questionnaire():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    print("Hello, ",name,"!")
    print("You are ",age," years old.")
    print("Your height is ",height,"meters.")
#questionnaire()

def questionnaire2():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")
    print(f"Your height is {height} meters.")
questionnaire2()
