#Given a string (a return value of input), isInteger will check whether the string can be converted into an integer.

def isInteger(value):
    try:
        int(value)
        return int(value) == float(value)
    except:
        return False

#print(isInteger('hi')) #f
#print(isInteger('42'))#t
#print(isInteger('2.4'))#f
#print(isInteger(2.4))#f
#print(isInteger(2))#t
