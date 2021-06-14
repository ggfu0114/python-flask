import random


class MathFunc:
    def __init__(self):
        self.default_num = 3

    def get_random_point(self):
        x_point = random.randint(1, 10)
        y_point = random.randint(1, 10)
        return (x_point, y_point)

    def get_triangle_size(self, point):
        size = point[0] * point[1] / 2
        return size
