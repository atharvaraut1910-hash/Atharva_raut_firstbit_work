# WAP to print grade based on given percentage (nested IF style)

per = int(input("Enter percentage: "))

if(per < 35):
    print("Fail")
else:
    if(per > 90):
        print("A")
    else:
        if(per > 80):
            print("B")
        else:
            if(per > 70):
                print("C")
            else:
                if(per > 35):
                    print("D")
