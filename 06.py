import urllib.request
import math
from turtlelab6 import turtle, home, shop, library, check

LAB = "turtlelab6.py"
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)

distance = lambda a, b: math.sqrt(a ** 2 + b ** 2)


def move(y2, y1, x2, x1):
    radian = lambda a, b: math.degrees(math.atan(a / b))
    turtle.left(radian(y2 - y1, x2 - x1))
    if x2 > x1:
        turtle.forward(distance(y2 - y1, x2 - x1))
    else:
        turtle.backward(distance(y2 - y1, x2 - x1))
    turtle.right(radian(y2 - y1, x2 - x1))


yhl, xhl = home.y - library.y, home.x - library.x
yhs, xhs = home.y - shop.y, home.x - shop.x

if distance(yhl, xhl) < distance(yhs, xhs):
    move(shop.y, turtle.y, shop.x, turtle.x)
    move(library.y, shop.y, library.x, shop.x)
    move(home.y, library.y, home.x, library.x)
else:
    move(library.y, turtle.y, library.x, turtle.x)
    move(shop.y, library.y, shop.x, library.x)
    move(home.y, shop.y, home.x, shop.x)

check()
