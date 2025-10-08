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
