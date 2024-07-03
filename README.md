## Basic_utils
Basic_utils is a toolkit(openCV) specifically designed for computer vision projects, offering a range of efficient and user-friendly tools and modules to accelerate development and enhance productivity. This repository includes practical functions for common operations 

Read an image and return it in *BGR* format.<br>
`image = readBGR('path/to/image.jpg')`

Read an image and return it in *RGB* format.<br>
`image = readRGB('path/to/image.jpg')`

Save an image to the specified file path.<br>
`save('path/to/save/image.jpg', image)`

Display an image in a window until any key is pressed.<br>
`show('Image Window', image)`

Convert a BGR format image to grayscale.<br>
`gray_image = BGR2Gray(image)`

Convert an RGB format image to grayscale.<br>
`gray_image = RGB2Gray(image)`

Convert a grayscale image to a three-channel fake color image (BGR).<br>
`color_image = Gray2Color(gray_image)`

Binarize an image.<br>
`binary_image = binarize(image, 127, 255)`

Resize an image to the specified width and height.<br>
`resized_image = resize_image(image, 200, 300)`

Rotate an image by the specified angle and scale.<br>
`rotated_image = rotate_image(image, 45)`

Apply Gaussian blur to an image.<br>
`blurred_image = blur_image(image, 5)`

Detect edges in an image.<br>
`edges = edge(image, 100, 200)`