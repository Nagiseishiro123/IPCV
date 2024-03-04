import cv2
import numpy as np

# Load the grayscale image
gray_image = cv2.imread('gray.jpg', cv2.IMREAD_GRAYSCALE)

# Create a temporary color image with equal color channels from the grayscale image
color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Create a color lookup table (LUT) matrix to combine the color channels
lut = np.zeros((256, 1, 3), dtype=np.uint8)

# Combine the color channels
lut[:, 0, 0] = np.arange(256)  # Green channel
lut[:, 0, 1] = 128             # Blue channel
lut[:, 0, 2] = np.flip(np.arange(256), axis=0)  # Red channel

# Apply the LUT to create a color image from the grayscale image
color_image = cv2.LUT(color_image, lut)

# Display the color image
cv2.imshow('Color Image', color_image)
cv2.imwrite('color_images/gray_to_color.jpg', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()