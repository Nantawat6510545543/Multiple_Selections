homework = int(input("Enter your homework percent: "))
midterm = int(input("Enter your midterm percent: "))
final = int(input("Enter your final percent: "))
score = homework * 0.1 + midterm * 0.4 + final * 0.5
print(f"Your total score is {score:.2f}.")

print("Your grade is ", end='')
if score >= 80:
    print("A.")
elif 75 <= score < 80:
    print("B+.")
elif 70 <= score < 75:
    print("B.")
elif 65 <= score < 70:
    print("C+.")
elif 60 <= score < 65:
    print("C.")
elif 55 <= score < 60:
    print("D+.")
elif 50 <= score < 55:
    print("D.")
else:
    print("F.")
