class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Addition of complex numbers
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # Subtraction of complex numbers
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # Multiplication of complex numbers
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

    def __str__(self):
        # String representation of the complex number
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"


# Input two complex numbers
print("Enter two complex numbers:")
c1_real = int(input("Real part of number 1: "))
c1_imag = int(input("Imaginary part of number 1: "))
c2_real = int(input("Real part of number 2: "))
c2_imag = int(input("Imaginary part of number 2: "))

# Create Complex objects
c1 = Complex(c1_real, c1_imag)
c2 = Complex(c2_real, c2_imag)

# Perform operations
addition_result = c1 + c2
subtraction_result = c1 - c2
multiplication_result = c1 * c2

# Display the results
print("The numbers are", c1, "and", c2)
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
