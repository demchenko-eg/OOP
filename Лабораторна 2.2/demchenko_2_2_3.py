import turtle
import random
import math

class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices
        self.median_intersection = None
        self.bisector_intersection = None

    def draw(self):
        turtle.penup()
        turtle.goto(self.vertices[0])
        turtle.pendown()
        turtle.goto(self.vertices[1])
        turtle.goto(self.vertices[2])
        turtle.goto(self.vertices[0])
        turtle.penup()

    def calculate_median_intersection(self):
        centroid_x = (self.vertices[0][0] + self.vertices[1][0] + self.vertices[2][0]) / 3
        centroid_y = (self.vertices[0][1] + self.vertices[1][1] + self.vertices[2][1]) / 3
        self.median_intersection = (centroid_x, centroid_y)

    def calculate_bisector_intersection(self):
        side1_midpoint_x = (self.vertices[1][0] + self.vertices[2][0]) / 2
        side1_midpoint_y = (self.vertices[1][1] + self.vertices[2][1]) / 2
        self.bisector_intersection = (side1_midpoint_x, side1_midpoint_y)

    def rotate_around_pivot(self, angle_degrees, pivot):
        rotated_vertices = []
        angle_radians = math.radians(angle_degrees)
        for vertex in self.vertices:
            x = pivot[0] + (vertex[0] - pivot[0]) * math.cos(angle_radians) - (vertex[1] - pivot[1]) * math.sin(angle_radians)
            y = pivot[1] + (vertex[0] - pivot[0]) * math.sin(angle_radians) + (vertex[1] - pivot[1]) * math.cos(angle_radians)
            rotated_vertices.append((x, y))
        self.vertices = rotated_vertices

    def scale_around_pivot(self, scale_factor, pivot):
        scaled_vertices = []
        for vertex in self.vertices:
            x = pivot[0] + (vertex[0] - pivot[0]) * scale_factor
            y = pivot[1] + (vertex[1] - pivot[1]) * scale_factor
            scaled_vertices.append((x, y))
        self.vertices = scaled_vertices

def generate_triangle():
    vertex1 = (random.uniform(-200, 200), random.uniform(-200, 200))
    vertex2 = (random.uniform(-200, 200), random.uniform(-200, 200))
    vertex3 = (random.uniform(-200, 200), random.uniform(-200, 200))
    return Triangle([vertex1, vertex2, vertex3])

def rotate_and_scale_animation(triangle, rotation_angle, scale_factor, total_frames):
    if rotation_angle < 360:
        turtle.clear()
        triangle.rotate_around_pivot(6, triangle.median_intersection)
        triangle.draw()
        turtle.update()
        turtle.ontimer(lambda: rotate_and_scale_animation(triangle, rotation_angle + 6, scale_factor, total_frames), 50)
    elif scale_factor <= 2:
        turtle.clear()
        triangle.scale_around_pivot(scale_factor, triangle.median_intersection)
        triangle.draw()
        turtle.update()
        turtle.ontimer(lambda: rotate_and_scale_animation(triangle, rotation_angle, scale_factor + 0.03, total_frames), 50)
    else:
        turtle.done()

def main():
    turtle.speed(1)
    turtle.hideturtle()
    turtle.tracer(0, 0)
    triangle = generate_triangle()
    triangle.calculate_median_intersection()
    triangle.calculate_bisector_intersection()
    turtle.ontimer(lambda: rotate_and_scale_animation(triangle, 0, 1, 100), 2000)
    turtle.mainloop()

if __name__ == "__main__":
    main()
