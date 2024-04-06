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
    



# if __name__ == "__main__":
#     r_list = RationalList()

#     r_list.append(Rational(1, 2))
#     r_list.append(Rational(3, 4))
#     r_list.extend([Rational(5, 6), Rational(7, 8)])
#     i = 2

#     print(r_list[0])
#     r_list[1] = Rational(9, 10)
#     print(r_list[1])
#     r_list[2] = Rational(11, 12)
#     print(r_list[2])
#     print(len(r_list))
#     result_list = r_list + 5
#     print(result_list)
#     result_list += r_list
#     print(result_list)