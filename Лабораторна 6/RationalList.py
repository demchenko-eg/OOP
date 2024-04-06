from Rational import Rational

class RationalList:
    def __init__(self, data=None):
        self.data = data if data is not None else []
    
    def __str__(self):
        return '[' + ', '.join(str(item) for item in self.data) + ']'
    
    def append(self, item):
        if type(item) == Rational:
            self.data.append(item)
    
    def extend(self, items):
        for item in items:
            self.append(item)

    def __setitem__(self, index, value):
        if type(value) == Rational:
            self.data[index] = value
        else:
            raise TypeError("Елементами списку можуть бути лише екземпляри класу Rational")

    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
    
    def __add__(self, other):
        if type(other) == RationalList:
            return RationalList(self.data + other.data)
        elif type(other) == Rational:
            return RationalList(self.data + [other])
        elif type(other) == int:
            return RationalList(self.data + [Rational(other, 1)])
    
    def __iadd__(self, other):
        if type(other) == RationalList:
            return RationalList(self.data + other.data)
        elif type(other) == Rational:
            return RationalList(self.data + [other])
        elif type(other) == int:
            return RationalList(self.data + [Rational(other, 1)])
        return self
    
    # def __iter__(self):
    #     sd = self.data[:]
    #     sd.sort(key=self.sort_key)
    #     return iter(sd)

    # def sort_key(self, r):
    #     return (-r.d, -r.n)
    



# if __name__ == "__main__":
#     new = []
#     r_list = RationalList([Rational(3, 4), Rational(1, 2), Rational(5, 8), Rational(7, 4)])
#     r_list.append(Rational(2, 3))
#     print(r_list)
#     for el in r_list:
#         new.append(el)
#         print(el)
#     print(new)