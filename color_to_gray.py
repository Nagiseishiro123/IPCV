import cv2

# Load color image
color_image = cv2.imread('pic.jpg')

# Convert color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('gray_images/color_to_gray.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()