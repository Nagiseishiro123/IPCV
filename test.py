import cv2
import numpy as np

# Create a color image from a grayscale image and color channels R, G, B
def gray_to_color(gray_image_path, r_channel_path, g_channel_path, b_channel_path):
    # Read the grayscale image
    gray_image = cv2.imread(gray_image_path, cv2.IMREAD_GRAYSCALE)

    # Read the color channels R, G, B
    r_channel = cv2.imread(r_channel_path, cv2.IMREAD_GRAYSCALE)
    g_channel = cv2.imread(g_channel_path, cv2.IMREAD_GRAYSCALE)
    b_channel = cv2.imread(b_channel_path, cv2.IMREAD_GRAYSCALE)

    # Combine the color channels to create a color image
    color_image = cv2.merge((b_channel, g_channel, r_channel))

    return color_image

# Save the color channels R, G, B from a color image
def save_color_channels(image_path):
    # Read the color image
    color_image = cv2.imread(image_path)

    # Split the color channels
    # b_channel, g_channel, r_channel = cv2.split(color_image)
    b_channel = color_image[:, :, 0]
    g_channel = color_image[:, :, 1]
    r_channel = color_image[:, :, 2]

    # Save the color channels as separate image files
    cv2.imwrite('r_channel.jpg', r_channel)
    cv2.imwrite('g_channel.jpg', g_channel)
    cv2.imwrite('b_channel.jpg', b_channel)

    print("Saved color channels R, G, B.")

# Main program
if __name__ == "__main__":
    # Save the color channels from a color image
    save_color_channels('pic.jpg')

    # Convert the grayscale image to a color image
    color_image = gray_to_color('gray_image.jpg', 'r_channel.jpg', 'g_channel.jpg', 'b_channel.jpg')

    # Display and save the color image from the grayscale image
    cv2.imshow('Color Image from Gray', color_image)
    cv2.imwrite('color_image_from_gray.jpg', color_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()