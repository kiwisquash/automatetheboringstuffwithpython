def isNumber(value):
    try:
        int(value)
        return int(value) == float(value)
    except:
        return False

#print(isNumber('hi')) #f
#print(isNumber('42'))#t
#print(isNumber('2.4'))#f
#print(isNumber(2.4))#f
#print(isNumber(2))#t
