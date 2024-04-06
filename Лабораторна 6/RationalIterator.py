from Rational import Rational

class RationalIterator:
    def __init__(self, rational):
        self.rational = rational
        self.sorted_pairs = sorted([(r.n, r.d) for r in rational], key=lambda x: (-x[1], -x[0]))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sorted_pairs):
            raise StopIteration
        n, d = self.sorted_pairs[self.index]
        self.index += 1
        return Rational(n, d)