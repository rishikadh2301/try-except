import math

try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    print(a/b)

except IndentationError:
    pass
except ValueError:
    print("a and b should be integers")

except ZeroDivisionError:
    print("b should not be 0")
except ImportError:
    print("check your code")



try:
    
    a="hello"
    print(a)
except NameError:                #print(b)
    print ("variable isnt defined")
except TypeError:                 #print(a+4)
    print("check ur code")
except ImportError:                # import maths
    print("import is not correct")
except ValueError:                 #print(int(a))
    print("a is not an integer")


try:
    x=int(input("enter x"))
    y=int(input("enter y"))
    print(x%y)
except ZeroDivisionError:
    print('y cannot be 0')

except ValueError:
    print("enter a value")

except Exception:
    print("there is an error")


def number():
    number=int(input("enter a number: "))
    if number>100 or number<0:
        # return "number is invalid
        raise ValueError("number is invalid")
    

try:
    number()
except ValueError:
    print("invalid")
