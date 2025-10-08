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