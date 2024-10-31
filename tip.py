check = input("Please put the amount of the check")
check = float(check)


tip_minus = check * 0.10
tip_medium = check * 0.15
tip_higher = check * 0.20

tip = input(
    "How much of tip do you want to leave? (1 to 10%), (2 to 15%), (3 to 20%)? "
)

tip = float(tip)

if tip == "1":
    print(f"{tip_minus:.2f}")
elif tip == "2":
    print(f"{tip_medium:.2f}")
elif tip == "3":
    print(f"{tip_higher:.2f}")
else:
    print("That number dont belong to any tip percent")

print("Thank you for the tip, I hope you enjoy the meal. Good night!")
