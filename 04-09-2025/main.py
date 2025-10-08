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
