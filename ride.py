ride = input("Which do you prefer? A car or a bike? ")
if ride == "car":
    subc = input("Electric or Gasoline? ")
    if subc == "electric":
        print("A Lotus Evija is a fantastic electric car.")
    elif subc == "gasoline":
        print("An Aventador is a classic.")
    else:
        print("Invalid. Choose electric or gasoline.")
elif ride == "bike":
    subb = input("Cruiser or Sports? ")
    if subb == "cruiser":
        print("The Classic 350 is the most popular choice.")
    elif subb == "sports":
        print("The Yamaha R15 V4 is a good choice.")
    else:
        print("Invalid. Choose cruiser or sports.")
else:
    print("Invalid. Choose car or bike.")