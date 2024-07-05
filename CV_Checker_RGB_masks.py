import cv2
import numpy as np
def red_mask(image_path):
    # 讀取圖像
    image = cv2.imread(image_path)
    image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
    # 轉換到HSV色彩空間
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定義紅色的HSV範圍
    red_lower1 = np.array([0, 70, 50])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([170, 70, 50])
    red_upper2 = np.array([180, 255, 255])
    # 創建遮罩以只檢測綠色
    red_mask1 = cv2.inRange(hsv_image, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv_image, red_lower2, red_upper2)
    mask_red = cv2.bitwise_or(red_mask1, red_mask2)
    mask_bright = cv2.inRange(hsv_image[:, :, 2], 170, 255)
    # 遮罩合併：紅色且亮度夠高
    mask = cv2.bitwise_and(mask_red, mask_bright)

    # 使用遮罩來提取紅色部分
    red_area = cv2.bitwise_and(image, image, mask= mask)
    return red_area

def green_mask(image_path):
    # 讀取圖像後轉換到HSV色彩空間
    image = cv2.imread(image_path)
    image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定義綠色的HSV範圍
    lower_green = np.array([35, 80, 50])
    upper_green = np.array([85, 255, 255])
    # 創建遮罩以只檢測綠色
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_bright = cv2.inRange(hsv_image[:, :, 2], 170, 255)
    # 遮罩合併：綠色且亮度夠高
    mask = cv2.bitwise_and(mask_green, mask_bright)

    # 使用遮罩來提取綠色部分
    green_area = cv2.bitwise_and(image, image, mask=mask)
    return green_area

def blue_mask(image_path):
    # 圖像轉換到HSV色彩空間
    image = cv2.imread(image_path)
    image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定義藍色的HSV範圍
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # 創建遮罩以只檢測藍色
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_bright = cv2.inRange(hsv_image[:, :, 2], 170, 255)
    # 遮罩合併：藍色且亮度夠高
    mask = cv2.bitwise_and(mask_blue, mask_bright)

    # 使用遮罩來提取藍色部分
    blue_area = cv2.bitwise_and(image, image, mask=mask)
    return blue_area

