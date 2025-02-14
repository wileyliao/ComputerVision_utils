import os
import cv2

# 讀取和處理圖片的函數
def pad_to_square(image, color=(0, 0, 0)):
    h, w = image.shape[:2]
    if h == w:
        return image
    size = max(h, w)
    top = (size - h) // 2
    bottom = size - h - top
    left = (size - w) // 2
    right = size - w - left
    padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return padded_image

# 主程式
def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            file_path = os.path.join(input_folder, filename)
            image = cv2.imread(file_path)
            if image is None:
                print(f"Failed to read {filename}. Skipping...")
                continue

            padded_image = pad_to_square(image)

            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, padded_image)
            print(f"Processed and saved: {output_path}")


# 設定輸入和輸出資料夾路徑
input_folder = r"C:\Projects\hw_num\cropped_num\augmented_images"  # 替換成你的圖片資料夾路徑
output_folder = r"C:\Projects\hw_num\cropped_num\augmented_image_padding"  # 替換成你想存放結果的資料夾

# 執行主程式
process_images(input_folder, output_folder)
