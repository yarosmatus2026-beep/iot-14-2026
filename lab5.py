from enum import Enum
import math
class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __del__(self):
        print("об'єкт видалено")
    def distance_to(self, other_point):
        d = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        return d
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x
    def get_y(self):
        return self.y
    def set_y(self, y):
        self.y = y
    def __str__(self):
        return f"точка складається з таких координат: {self.x}, {self.y}"
class Polynom:
    def __init__(self, colour, *points):
        self.colour = colour
        self.points = list(points)
    def get_perimetr(self):
        perimetr = 0
        n = len(self.points)
        for num in range(n-1):
            curr_point = self.points[num]
            next_point = self.points[num+1]
            perimetr += curr_point.distance_to(next_point)
        perimetr += self.points[-1].distance_to(self.points[0])
        return perimetr
    def get_longest_diagonal(self):
        n = len(self.points)
        longest_diagonal = 0
        if n < 4:
            return 0
        for i in range(n):
            for j in range(i + 1, n):
                if j == i + 1 or (i == 0 and j == n - 1):
                    continue
                diagonal = self.points[i].distance_to(self.points[j])
                if diagonal > longest_diagonal:
                    longest_diagonal = diagonal
        return longest_diagonal
    def sort_x(self):
        def get_x(p):
            return p.x
        self.points.sort(key=get_x)
    def sort_y(self):
        def get_y(p):
            return p.y
        self.points.sort(key=get_y)
    def __del__(self):
        print("об'єкт видалено")
    def __str__(self):
        res = f"Поліном {self.colour} складається з точок: "
        for p in self.points:
            res += f"({p.x}, {p.y})"
        return res
def main():
    pt1 = Point(5, 1)
    print(pt1)
    pt2 = Point(6, 8)
    pt3 = Point(8, 12)
    pt4 = Point(4, 11)
    pt5 = Point(6, 0)
    pt6 = Point(118, 118)
    
    poly1 = Polynom(Colour.RED, pt5, pt4, pt3, pt2)
    res1 = poly1.get_longest_diagonal()
    print(f"У {poly1} Найдовша діагональ: {round(res1, 2)}")
    per1 = poly1.get_perimetr()
    print("Периметр:", per1)
    
    poly2 = Polynom(Colour.GREEN, pt4, pt1, pt3, pt2, pt5)
    res2 = poly2.get_longest_diagonal()
    print(f"У {poly2} Найдовша діагональ: {round(res2, 2)}")
    per2 = poly2.get_perimetr()
    print("Периметр:", per2)
    
    poly3 = Polynom(Colour.PURPLE, pt1, pt2, pt3, pt4, pt5)
    res3 = poly3.get_longest_diagonal()
    print(f"У {poly3} Найдовша діагональ: {round(res3, 2)}")
    per3 = poly3.get_perimetr()
    print("Периметр:", per3)

    poly4 = Polynom(Colour.PURPLE, pt1, pt2, pt3, pt6)
    res4 = poly4.get_longest_diagonal()
    print(f"У {poly4} Найдовша діагональ: {round(res4, 2)}")
    per4 = poly4.get_perimetr()
    print("Периметр:", per4)
main()