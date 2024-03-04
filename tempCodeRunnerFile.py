import cv2
import numpy as np

# Tải ảnh xám
gray_image = cv2.imread('gray.jpg', cv2.IMREAD_GRAYSCALE)

# Tạo một ảnh màu tạm thời với các kênh màu giống nhau từ ảnh xám
color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# Tạo một ma trận màu để kết hợp các kênh màu
lut = np.zeros((256, 1, 3), dtype=np.uint8)

# Kết hợp các kênh màu
lut[:, 0, 0] = np.arange(256)  # Kênh màu xanh lá cây
lut[:, 0, 1] = 128             # Kênh màu xanh dương
lut[:, 0, 2] = np.flip(np.arange(256), axis=0)  # Kênh màu đỏ

# Áp dụng LUT để tạo ảnh màu từ ảnh xám
color_image = cv2.LUT(color_image, lut)

# Hiển thị ảnh màu
cv2.imshow('Color Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()