import os
import cv2

def readBGR(filepath):
    return cv2.imread(filepath)

def readRGB(filepath):
    image = cv2.imread(filepath)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

def save(filepath, image):
    cv2.imwrite(filepath, image)

def show(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def BGR2Gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def RGB2Gray(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def Gray2Color(gray_image):
    fake_rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    return fake_rgb_image

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def rotate_image(image, angle, scale=1.0):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, rotation_matrix, (w, h))

def blur_image(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def edge(image, threshold1, threshold2):
    return cv2.Canny(image, threshold1, threshold2)

def binarize(image, threshold, max_value):
    _, binary_image = cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY)
    return binary_image

