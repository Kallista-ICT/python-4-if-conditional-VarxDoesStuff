Score = int(input("Please enter your score: "))

if Score < 50:
    Category_Name = "F"
elif Score < 60:
    Category_Name = "D"
elif Score < 75:
    Category_Name = "C"
elif Score < 85:
    Category_Name = "B"
else:
    Category_Name = "A"

print(f"The category is: {Category_Name}")