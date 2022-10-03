x = float(input("Enter a real number: "))

if x <= 15:
    ans = 2 * x + 10
elif 15 < x <= 35:
    ans = 3 * (x ** 2)
else:
    ans = 2 * (x ** 3) - 5

print(f"f({x:.3f}) = {ans:.3f}")
