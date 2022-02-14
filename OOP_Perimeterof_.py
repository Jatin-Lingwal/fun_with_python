"""using OOP calculating triangle perimeter"""
class Tringale:
    def __init__(self,a ,b, c):
        self.a = a
        self.b = b
        self.c = c
    def Perimeter(self):
        P = self.a + self.b + self.c
        return P
tringle1 = Tringale(2, 3, 4)
P = tringle1.Perimeter()
print("Perimeter of a triangle will be:", P)




