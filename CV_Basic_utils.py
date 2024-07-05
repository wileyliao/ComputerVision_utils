import cv2

def readBGR(filepath):
    """
        param:
            filepath (str): Path to the image file.

        return:
            numpy.ndarray: The read image in BGR format.
    """
    return cv2.imread(filepath)

def readRGB(filepath):
    """
        param:
            filepath (str): Path to the image file.

        return:
            numpy.ndarray: The read and converted image in RGB format.
    """
    image = cv2.imread(filepath)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

def save(filepath, image):
    """
        param:
            filepath (str): Path to save the image file.
            image (numpy.ndarray): The image to be saved.
    """
    cv2.imwrite(filepath, image)

def show(window_name, image):
    """
        param:
            window_name (str): Name of the window.
            image (numpy.ndarray): The image to be displayed.
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def BGR2Gray(image):
    """
        param:
            image (numpy.ndarray): The BGR format image.

        return:
            numpy.ndarray: The grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def RGB2Gray(image):
    """
        param:
            image (numpy.ndarray): The RGB format image.

        return:
            numpy.ndarray: The grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def Gray2Color(gray_image):
    """
        param:
            gray_image (numpy.ndarray): The grayscale image.

        return:
            numpy.ndarray: The fake color image (BGR format).

    """
    fake_rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    return fake_rgb_image
def binarize(image, threshold, max_value):
    """
        param:
            image (numpy.ndarray): The original image.
            threshold (float): The threshold value for binarization.
            max_value (float): The maximum value for the binarized image.

        return:
            numpy.ndarray: The binarized image.
    """
    _, binary_image = cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY)
    return binary_image

def resize_image(image, width, height):
    """
        param:
            image (numpy.ndarray): The original image.
            width (int): The width of the new image.
            height (int): The height of the new image.

        return:
            numpy.ndarray: The resized image.
    """
    return cv2.resize(image, (width, height))

def rotate_image(image, angle, scale=1.0):
    """
        param:
            image (numpy.ndarray): The original image.
            angle (float): The rotation angle.
            scale (float, optional): The scale factor, default is 1.0.

        return:
            numpy.ndarray: The rotated image.
    """
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, rotation_matrix, (w, h))

def blur_image(image, kernel_size):
    """
        param:
            image (numpy.ndarray): The original image.
            kernel_size (int): The size of the blur kernel, must be a positive odd number.

        return:
            numpy.ndarray: The blurred image.
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def edge(image, threshold1, threshold2):
    """
        param:
            image (numpy.ndarray): The original image.
            threshold1 (float): The first threshold for edge detection.
            threshold2 (float): The second threshold for edge detection.

        return:
            numpy.ndarray: The image with detected edges.
    """
    return cv2.Canny(image, threshold1, threshold2)


