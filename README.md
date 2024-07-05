## CV_Basic_utils

Read image in *BGR* format.
`image = readBGR('path/to/image.jpg')`<br>
Read image in *RGB* format.
`image = readRGB('path/to/image.jpg')`<br>
Save image.
`save('path/to/save/image.jpg', image)`<br>
Display image.
`show('Image Window', image)`<br>
Convert BGR to gray.
`gray_image = BGR2Gray(image)`<br>
Convert RGB to grayscale.
`gray_image = RGB2Gray(image)`<br>
Convert gray to fake color image.
`color_image = Gray2Color(gray_image)`<br>
Binarize image.
`binary_image = binarize(image, 127, 255)`<br>
Resize image.
`resized_image = resize_image(image, 200, 300)`<br>
Rotate image.
`rotated_image = rotate_image(image, 45)`<br>
Gaussian blur.
`blurred_image = blur_image(image, 5)`<br>
Canny edge.
`edges = edge(image, 100, 200)`<br>

## CV_Checker
是一個用於影像處理的工具集，包含多種功能來檢測和調整圖像中的不同屬性。
### Binarize_threshold
此模組提供了調整圖像二值化閾值的功能。通過不同的閾值範圍來觀察圖像的二值化效果，方便選擇最佳的閾值設定。
### Canny_threshold
此模組用於執行 Canny 邊緣檢測，通過調整高低閾值來觀察不同閾值組合對邊緣檢測結果的影響，從而選擇最適合的參數設定。
### Dominant_Color
此模組用於檢測圖像中的主要顏色。通過轉換到 HSV 色彩空間並應用顏色範圍，模組可以找出圖像中佔據面積最大的顏色部分，並返回主要顏色。
### HSV_value
此模組透過迴圈調整圖像的 HSV 值來生成不同效果的圖像。調整後的圖像和邊緣檢測結果將被輸出並保存，方便用戶觀察 HSV 值變化對圖像效果的影響。
### RGB_masks
此模組提供了生成紅色、綠色和藍色遮罩的功能。提取出圖像中對應顏色的部分，方便後續的處理和分析。

## CV_Drawer
此模組通過滑鼠操作在圖像上選擇矩形區域，並顯示選定的矩形區域座標。