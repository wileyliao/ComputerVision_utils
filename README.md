# ComputerVision_utils
ComputerVision_utils is a toolkit(openCV) specifically designed for computer vision projects, offering a range of efficient and user-friendly tools and modules to accelerate development and enhance productivity. This repository includes practical functions for common operations 

### Read an image and return it in *BGR* format.
```python
def readBGR(filepath):
    """
    param:
        filepath (str): Path to the image file.
    
    return:
        numpy.ndarray: The read image in BGR format.
    """
    return cv2.imread(filepath)
```
`image = readBGR('path/to/image.jpg')`

### Read an image and return it in *RGB* format.
```python
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
```
`image = readRGB('path/to/image.jpg')`

### Save an image to the specified file path.
```python
def save(filepath, image):
    """    
    param:
        filepath (str): Path to save the image file.
        image (numpy.ndarray): The image to be saved.
    """
    cv2.imwrite(filepath, image)
```
`save('path/to/save/image.jpg', image)`

### Display an image in a window until any key is pressed.
```python
def show(window_name, image):
    """   
    param:
        window_name (str): Name of the window.
        image (numpy.ndarray): The image to be displayed.    
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
`show('Image Window', image)`

### Convert a BGR format image to grayscale.
```python
def BGR2Gray(image):
    """
    param:
        image (numpy.ndarray): The BGR format image.
    
    return:
        numpy.ndarray: The grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```
`gray_image = BGR2Gray(image)`

### Convert an RGB format image to grayscale.
```python
def RGB2Gray(image):
    """
    param:
        image (numpy.ndarray): The RGB format image.
    
    return:
        numpy.ndarray: The grayscale image.
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
```
`gray_image = RGB2Gray(image)`

### Convert a grayscale image to a three-channel fake color image (BGR).
```python
def Gray2Color(gray_image):
    """
    param:
        gray_image (numpy.ndarray): The grayscale image.
    
    return:
        numpy.ndarray: The fake color image (BGR format).

    """
    fake_rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    return fake_rgb_image
```
`color_image = Gray2Color(gray_image)`

### Binarize an image.
```python
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
```
`binary_image = binarize(image, 127, 255)`

### Resize an image to the specified width and height.
```python
def resize(image, width, height):
    """
    param:
        image (numpy.ndarray): The original image.
        width (int): The width of the new image.
        height (int): The height of the new image.
    
    return:
        numpy.ndarray: The resized image.
    """
    return cv2.resize(image, (width, height))
```
`resized_image = resize_image(image, 200, 300)`

### Rotate an image by the specified angle and scale.
```python
def rotate(image, angle, scale=1.0):
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
```
`rotated_image = rotate_image(image, 45)`

### Apply Gaussian blur to an image.
```python
def blur_image(image, kernel_size):
    """
    param:
        image (numpy.ndarray): The original image.
        kernel_size (int): The size of the blur kernel, must be a positive odd number.
    
    return:
        numpy.ndarray: The blurred image.
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
```
`blurred_image = blur_image(image, 5)`

###  Detect edges in an image.
```python
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
```
`edges = edge(image, 100, 200)`