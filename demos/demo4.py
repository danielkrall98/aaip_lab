import aaip.ex4 as ex4

def demo():
    # Create some complex numbers
    c1 = ex4.ComplexNumber(3, 2)  # 3 + 2i
    c2 = ex4.ComplexNumber(1, -4)  # 1 - 4i

    # Demonstrate arithmetic operations
    print("Addition:", c1 + c2)  # Output: 4 - 2i
    print("Subtraction:", c1 - c2)  # Output: 2 + 6i
    print("Multiplication:", c1 * c2)  # Output: 11 - 10i
    print("Division:", c1 / c2)  # Output: -0.4 + 0.8i

    # Summing a list of complex numbers
    complex_list = [c1, c2, ex4.ComplexNumber(2, 3)]  # 3 + 2i, 1 - 4i, 2 + 3i
    total = ex4.sum_complex_numbers(complex_list)
    print("Sum of complex numbers:", total)  # Output: 6 + 1i

if __name__ == "__main__":
    demo()
