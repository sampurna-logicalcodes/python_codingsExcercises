#2.Define a function that returns if multipied first two parameter values and resulted value of last digit exulas to third element

def last_digit(a,b,c):
    return str(a*b)[-1] == str(c)[-1]
print(last_digit(12,2,4))
print(last_digit(32,23,34))