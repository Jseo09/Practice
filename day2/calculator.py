def multiply(input1, input2):
    return input1 * input2
def divide(input1, input2):
    if input2 == 0:
        print("Error: Division by zero is not allowed.")
        return input1
    return input1/input2
def addition(input1, input2):
    return input1+input2
def subtraction(input1, input2):
    return input1-input2
initiate = True 
number = 0
operators = ["+","-","*","/"]
while True: 
    if initiate:
        input1 = float(input("What's the first number? : "))
        number+=input1
        initiate=False

    for x in operators:
        print(x)
    operation = input("Please select one from this operators")
    if operation in operators: 
        pass
    else: 
        print("invalid choice! ending the program")
        break 
    input2 = float(input("What is the second number? : "))
    if operation == "+":
        number = addition(number,input2)
    elif operation == "-":
        number = subtraction(number, input2)
    elif operation == "*":
        number = multiply(number,input2)
    else:
        number = divide(number,input2)
    print(number)
    quit = input("Do you want to continue? type 'y' for yes and 'n' for no ").lower()
    if quit == 'y':
        continue 
    else: 
        break
