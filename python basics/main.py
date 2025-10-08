a = int(input("enter a :"))
print(a)



x = (a*10/100)
y = (a*5/100)

if a >= 1000 :
     print(a-x)

elif a >= 500 and a <= 1000 :
    print(a-y)

elif a >= 500 :
    print("no discount")


a = int(input("enter neymar jersey no :"))
print(a)

b = int(input("enter messi jersey no :"))
print(b)

c = int(input("enter ronaldo jersey no :"))
print(c)

if a < b :
   print("neymar is goat")

else :
    print("goat Neymar")


animal = input("enter name :")

if animal == "red" :
   print("stop")

elif animal == "grren" :
   print("ready")

elif animal == "yellow" :
   print("go")


month = int( input("enter month(1-12) :"))

match month:
     case 12 | 1 | 2 :
    print("winter season")
     case 3|4|5 :
    print("summer")
     case 6|7|8|9 :
    print("monsoon")
     case 11|12 :
    print("autumn")
     case _ :
    print("Neymar GOAT")


   month = int(input("Enter month number:"))

match month:
    case 12 | 1 | 2:
        print("❄️ Winter Season")
    case 3 | 4 | 5:
        print("🌸 Spring Season")
    case 6 | 7 | 8:
        print("☀️ Summer Season")
    case 9 | 10 | 11:
        print("🍂 Autumn (Fall) Season")
    case _:
        print("❌ Invalid month number")



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


Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
Sample Testcase :
INPUT
9 2
OUTPUT
odd

m = int(input("Enter any number: "))
n = int(input("Enter any value: "))

total = m + n  

if total % 2 == 0:
    print("even")
else:
    print("odd")


n = int(input("enter n :"))

num1 = int(input("enter  value :"))
num2 = int(input("enter value :"))

m = num1 + num2
j = num1 * num2

if m + j == n:

    print("great")

else :
    print("small")




D = int(input("enter diatance :"))

if 5 >= D :
    print(D * 10)

elif 6 <= D and D <= 15: 
    print(D * 8)

else :
    print(D * 6)

if D == 50:
    print("50 rs only")


Write a program that takes a number as input and prints:
"Fizz" if the number is divisible by 3.
"Buzz" if the number is divisible by 5.
"FizzBuzz" if the number is divisible by both 3 and 5.


r = int( input("enter value :"))

if r%3 == 0 and r%5 == 0 :
    print("fizzbuzz")

elif r%3 == 0:
    print("fizz")

elif r%5 == 0:
    print("buzz")

else : 
    print("neymar")




A triangle can be classified based on its sides as:
Equilateral → all three sides are equal.
Isosceles → any two sides are equal.
Scalene → all three sides are different.



a = int(input("enter value :"))
b = int(input("enter value :"))
c = int(input("enter value :"))

if a == b < c or b == c < a or c == a < b:
    print("Not a valid triangle")


elif a == b == c:
    print("equilateral")

elif a == b or b  == c or a == c:
    print("Isosceles")
    

else :
    print("Scalene")



a = input("science,arts,commerce")

m = 10
n = int(input("enter any value\n"))

while n <= m :
    print(n*n*n)
    n = n + 1  

a = int(input("Enter a number: "))       
b = int(input("Enter how many numbers to print: "))  
c = 0   
while c < b:
    print(a + c)
    c += 1





n = 6     # first 5 numbers
i = 1       # counter
sum = 0

while i <= n:
    sum += i   # sum = sum + i
    i += 1

    average = sum / n
print("Average =", average)






a = 4
b = 11

for i in range(b,a-1,-1):
    print(i)




a = 1
b = 5

for i in range(a,b+1)

n = int(input("enter number"))
a = 1
b = 2

while a <= n:
    print(b)
    b = b *2
    a = a +1


a = 1
n = 10

while a <= n:
    print(a*a)
    a = a + 1

n = int(input("from user"))
a = 1
b = 0

while a <= b:
    

score = int(input("enter value\n"))

if score >= 90 and score <= 100:
    print("padipali")

elif score >= 80 and score <= 89:
    print("mid padipali")

elif score >= 70 and score <= 79:
    print("average")

elif score >= 60 and score <= 69:
    print("normal")

else :
    print("veliya poda")

score = int(input("enter value\n"))

if score >= 90:
    print("topper")

elif score >=80:
    print("better")

elif score >=70:
    print("mid")

elif score >= 60:
    print("average")

elif score >=50:
    print("ok")

else:
    print("NEYMAR")


a = int(input("enter value\n"))
b = int(input("enter value\n"))
c = int(input("enter value\n"))

if a > b and c < a:
    print("Ronaldo")

elif b > a and c < b :
    print("messi ")

else :
    print("neymar")


n = int(input("enter value\n"))

for i in range (1,n+1):
    print(i**3,end =" ")



1 st problem for task

a = int(input("Enter Value \n"))

if a%4 == 0 :
    print("yes")

else :
    print("no")


2 problem for test







a = int(input("enter value\n"))
b = int(input("enter value\n"))

sum_even = 0
num = a

while num <= b:
    if num % 2 == 0:
        sum_even += num
    num += 1

print(sum_even)



age = int(input("from me\n"))

if age >= 0 and age <=18:
    print(150)
elif age > 18 and age <= 60:
    print(250)
elif age > 60:
    print(100)

else:
    print("wrong input bro")



A stadium sells entry passes with the following rules:
* If age < 12 → Ticket = ₹50
* If age between 12–59 → Ticket = ₹120
* If age ≥ 60 → Ticket = ₹80

a = int(input("from user\n"))

if a >= 0 and a <= 12 :
    print(50)
elif a >= 13 and a <= 59 :
    print(120)
elif a > 59 :
    print(80)
else : 
    print("invalied")


A shopkeeper has n mangoes.
He wants to pack them into baskets, with 5 mangoes in each basket.
Write a program to calculate:
* How many full baskets can be made
* How many mangoes will be left


n = int(input("enter\n"))

basket = n // 5 
remain = n % 5

print(basket)
print(remain)


n = int(input("from user\n"))
days = int(input("from user\n"))
while n > 0 :
    n = n-1
    days-=1
    print("days", n)
    
salary = int(input("from user\n"))
sales = int(input("from user\n"))

if sales >= 100 :
    bonus = salary / 10
elif sales >= 50 and sales <= 99 :
    bonus = salary / 5
elif sales < 50 :
    print("no")


print(bonus + salary)

sales = int(input("Enter amount: "))

if sales <= 5000:
    commission = sales * 5 / 100   
elif sales <= 10000:               
    commission = sales * 10 / 100  
else:                              
    commission = sales * 15 / 100  


print("Commission =", commission)


price = int(input("from nanbar\n"))

if price > 100 :
    discount = price / 10
elif price > 50 and price < 100 :
    discount = price / 5

print(discount)


coach_number = int(input("Enter coach number: "))

Check if the number is valid
if coach_number > 10 or coach_number < 1:
    print("Invalid")
elif coach_number % 2 == 0:
    print("AC coach")
else:
    print("Sleeper coach")



distance = float(input("Enter distance covered (in km): "))
fuel = float(input("Enter fuel used (in liters): "))


mileage = distance / fuel


if mileage > 0:
    print("Excellent")

elif mileage >= 30 and mileage <= 50:
        print("Average")
else:
        print("No")

    

