from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image = Image.open('lone tree.jpg')
gray_image = image.convert('L')
gray_array = np.array(gray_image)
plt.subplot(1, 2, 1)
plt.imshow(np.array(image))
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(gray_array, cmap='gray')
plt.title('Grayscale Image')
plt.show()