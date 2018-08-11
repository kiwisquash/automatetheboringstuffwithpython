# This program allows me to store as many cat names as I like.
# After I've finished entering all the names, the program will list all the names out.

catNames = []
print("Please enter the name of a cat.")
print("If you don't want to add any cat names, hit enter without typing anything.")
catName = input()
while catName !="":
    catNames = catNames + [catName]
    print("Would you like to enter another cat name?\n")
    print("If you don't want to add any cat names, hit enter without typing anything.")
    catName = input()
if len(catNames)==0:
    print("You didn't enter any cat names!")
else:
    print("You entered " + str(len(catNames)) + " cat names.\nThey are:")
    for catName in catNames:
        print("\t"+catName)

