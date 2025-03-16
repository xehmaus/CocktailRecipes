class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        print(self.r, '+i',self.i)
         
    def display(self):       
         print(self.r, '+i',self.i)
         
if __name__ == "__main__":
    
    A = Complex(1,2)