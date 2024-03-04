import cv2

# Load color image
color_image = cv2.imread('pic.jpg')

# Split color channels
B, G, R = cv2.split(color_image)

# Define weights
alpha = 0.299
beta = 0.587
gamma = 0.114

# Compute gray pixel values using formula
gray_image = alpha * R + beta * G + gamma * B

# Convert gray image to uint8 data type
gray_image = gray_image.astype('uint8')

# Display grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('gray_images/color_to_gray2.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()