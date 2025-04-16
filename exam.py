medc = input("Do you have a medical cause? Y or N: ")
att = int(input("What is your attendance percentage? "))
if medc == "N":
    if att >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")
elif medc == "Y":
    print("You are eligible for the exam.")
else:
    print("Invalid. Please enter Y for yes and N for no.")