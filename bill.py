unit = int(input("Enter units consumed: "))
if unit < 50:
    print("Your Electricity bill is ", (unit*2.6)+25)
elif unit >=50 and unit < 100:
    print("Your electricity bill is ", (unit*3.25)+35)
elif unit >= 100 and unit < 200:
    print("Your electricity bill is ", (unit*5.26)+45)
else:
    print("Your electricity bill is ", (unit*8.45)+75)