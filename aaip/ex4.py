class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real**2 + other.imaginary**2
            if denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
            imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented
    
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
        
    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imaginary})"
    
    def sum_complex_numbers(complex_list):
        return sum([c for c in complex_list], start=ComplexNumber(0, 0))