print("Input a point (x,y):")
x = int(input("x = ? "))
y = int(input("y = ? "))

text = ["origin", "quadrant 1", "quadrant 2", "quadrant 3", "quadrant 4", "y-axis", "x-axis"]
position = ["at the", "on the", "in"]
n = 2
if x == 0:
    n = 1
    if y == 0:
        i = 0
        n = 0
    else:
        i = 5
elif y == 0:
    n = 1
    i = 6

elif x > 0:
    if y > 0:
        i = 1
    else:
        i = 4

elif x < 0:
    if y < 0:
        i = 3
    else:
        i = 2

print(f"The point ({x:.2f},{y:.2f}) is {position[n]} {text[i]}.")
