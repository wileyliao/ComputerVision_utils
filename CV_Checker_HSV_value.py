#迴圈調整一張圖片的hsv值並輸出存檔觀測結果
import cv2
import numpy as np
import os

# 讀取圖像
image_path = './testimg/g05.jpg'
image = cv2.imread(image_path)
image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 確保輸出目錄存在
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 疊代色調、飽和度和亮度
for h in range(0, 180, 20):  # 色調從 0 到 180
    for s in range(0, 256, 20):  # 飽和度從 0 到 255
        for v in range(0, 256, 20):  # 亮度從 0 到 255
            # 複製HSV圖像進行調整
            adjusted_hsv = hsv_image.copy()
            adjusted_hsv[:, :, 0] = (adjusted_hsv[:, :, 0] + h) % 180
            adjusted_hsv[:, :, 1] = np.clip(adjusted_hsv[:, :, 1] + s - 128, 0, 255)
            adjusted_hsv[:, :, 2] = np.clip(adjusted_hsv[:, :, 2] + v - 128, 0, 255)

            # 轉回BGR格式並保存圖像
            adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
            gray = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 5)
            edges = cv2.Canny(blurred, 40, 150)

            trans_filename = f'h{h}_s{s}_v{v}.jpg'
            edge_filename = f'h{h}_s{s}_v{v}_edge.jpg'
            cv2.imwrite(os.path.join(output_dir, trans_filename), adjusted_image)
            cv2.imwrite(os.path.join(output_dir, edge_filename), edges)

            print(f'h{h}_s{s}_v{v}_done')

print("Image saved at:", output_dir)
