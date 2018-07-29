# This program says hello and asks for my name, age, then tells me how old I will be in a year.

print("Hello world!")
name = input("What is your name? ")
print("It is good to meet you, "+name+".")
print("The length of your name is",end=": ")
print(len(name))
age = int(input("What is your age? "))+1
print(name + ", you are going to be "+str(age)+" in a year!")

