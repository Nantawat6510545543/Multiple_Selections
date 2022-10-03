def is_child(height):
    return height <= 120


def read_height():
    return float(input("Enter height: "))


def print_result(child):
    if child:
        print("Child")
    else:
        print("Adult")


tall = read_height()
check = is_child(tall)
print_result(check)
