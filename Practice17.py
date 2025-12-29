# WAP RECIVE TWO NUMBER FROM USER INA  FUCNTION AND RETURN THE RESULT OF ALL ARITHEMATIC OPERATORS 
# OF THOSE NUMBERS (+,-,*,/,%)

def calc(x,y):
    return x+y , x-y , x*y , x/y , x%y
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
add , sub , mul , div , mod = calc(num1,num2)
print("Sum = " , add)
print("subtract = " , sub)
print("multiply = " , mul)
print("Division = " , div)
print("Modulo = " , mod)