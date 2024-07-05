import cv2
import numpy as np

def find_dominant_color(image_path):
    # 讀取圖像並轉換到HSV色彩空間
    image = cv2.imread(image_path)
    image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定義不同顏色的HSV閾值範圍，特別注意紅色的兩個範圍
    color_ranges = {
        'red1': (np.array([0, 50, 50]), np.array([10, 255, 255])),
        'red2': (np.array([170, 50, 50]), np.array([180, 255, 255])),
        'green': (np.array([35, 50, 50]), np.array([85, 255, 255])),
        'blue': (np.array([100, 150, 50]), np.array([140, 255, 255]))
    }

    max_area = 0
    dominant_color = None

    # 紅色需要特別處理，將兩個區域的面積相加
    red_area = 0

    # 為每種顏色應用閾值，找出佔最大範圍的顏色
    for color, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv_image, lower, upper)
        area = cv2.countNonZero(mask)  # 計算掩碼中非零像素的數量，即該顏色的面積

        # 累加紅色的面積
        if 'red' in color:
            red_area += area
            if red_area > max_area:
                max_area = red_area
                dominant_color = 'red'
        else:
            if area > max_area:
                max_area = area
                dominant_color = color

    return dominant_color
