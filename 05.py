AD = int(input("Enter year in AD: "))

if AD <= 0:
    print("Invalid input: use positive integer")
elif AD < 1752 and AD % 4 == 0:
    print(f"AD {AD} is a leap year")
else:
    if AD % 400 == 0:
        print(f"AD {AD} is a leap year")
    elif AD % 4 == 0 and AD % 100 != 0:
        print(f"AD {AD} is a leap year")
    else:
        print(f"AD {AD} is not a leap year")

