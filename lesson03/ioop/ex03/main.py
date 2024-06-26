from circle import Circle
from rectangle import Rectangle
from shape import Shape


def main():
    shape_a = Shape('red')
    circle_a = Circle('blue', 3)
    rectangle_a = Rectangle('yellow', 2, 4)

    print(shape_a.color)
    print(f"{circle_a.color} - {circle_a.area()}")
    print(f"{rectangle_a.color} - {rectangle_a.area()}")

main()