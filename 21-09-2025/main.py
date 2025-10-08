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

