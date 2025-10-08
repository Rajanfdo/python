a = 100
b = 30
c = 50

if b > a and b > c:
    print(b)

elif c > a and c > b:
    print(c)

else :
    print(a)

x = 200
y = 10
z = 30

(a,b,c) = (200,10,30)
print(max(a,b,c))


x = int(input("enter :"))

if x <=0 and x >= 10:
    print("small")

elif x <=50 and x >= 10:
    print("medium")

elif x <= 100 and x >= 50:
    print("NEYMAR GOAT")


def calculator(operator, number1, number2):

    
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))

    match operator:
        case '+':
            print(number1 + number2)
        case '-':
            print(number1 - number2)
        case '*':  
            print(number1 * number2)
        case '/':
                print(number1 / number2)
        case _: 
            print("Invalid operator")