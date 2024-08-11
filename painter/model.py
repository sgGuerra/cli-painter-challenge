import math
import  matplotlib.pyplot as plt

class Point:
    def __init__(self, x: float, y:float ):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius


    def area(self):
        return float(math.pi*(self.radius**2))


    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()


    def __str__(self):
        return f"Circle with center at ({self.center.x}, {self.center.y}) and radius {self.radius}"


class Triangle:
    def __init__(self,point_1: Point, point_2: Point, point_3: Point ):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3


    def area(self):




