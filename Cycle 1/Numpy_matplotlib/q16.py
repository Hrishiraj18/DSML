import matplotlib.pyplot as plt
complex_number = 1.5 + 2.5j
real_part = complex_number.real
imaginary_part = complex_number.imag
plt.figure(figsize=(6, 6))
plt.scatter(real_part, imaginary_part, color='red', marker='o', label='Complex Number')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.title('Complex Number Plot')
plt.show()
