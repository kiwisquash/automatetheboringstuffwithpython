from inputValidator import isInteger 

def collatz(value):
    if value % 2 == 0:
        return value // 2
    if value % 2 == 1:
        return 3*value + 1 

print("Please enter an integer:",end=" ")
userInput = input()
while not isInteger(userInput):
    print("You didn't enter an integer.")
    print("Please enter an integer:",end=" ")
    userInput = input()
value = int(userInput)
print(value)
while (value !=1):
    value = collatz(value)
    print(value)
