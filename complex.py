"""
고관성: maintainer, multiplication
신혜지: addition, subtraction
"""
class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
        
    def __str__(self):
        return str(self.re)+"+"+str(self.im)+"i"
        
c1 = Complex(1,2)
print(c1)

