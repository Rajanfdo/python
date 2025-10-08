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