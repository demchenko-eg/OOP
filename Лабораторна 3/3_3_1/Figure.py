class Figure:
    def __init__(self, dim):
        self.dim = dim

    def dimension(self):
        return self.dim

    def perimeter(self):
        raise NotImplementedError("perimeter method should be implemented in subclasses")

    def square(self):
        raise NotImplementedError("square method should be implemented in subclasses")

    def surface_area(self):
        raise NotImplementedError("surface_area method should be implemented in subclasses")

    def base_area(self):
        raise NotImplementedError("base_area method should be implemented in subclasses")

    def height(self):
        raise NotImplementedError("height method should be implemented in subclasses")

    def volume(self):
        raise NotImplementedError("volume method should be implemented in subclasses")