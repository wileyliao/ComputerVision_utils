import CV_Basic_utils as iu
import os


input_folder = 'path/to/RGBimage/folder'
output_folder = 'path/to/fakeRGBimage/save/folder'

def process_images(input_dir, output_dir):
    # 確保輸出目錄存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 讀取輸入目錄中的所有圖片文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 構建完整的文件路徑
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # 讀取圖片
            image = iu.readBGR(input_path)
            # 轉換為灰階圖片
            gray_image = iu.BGR2Gray(image)

            # 轉換為假RGB圖片
            fake_rgb_image = iu.Gray2Color(gray_image)

            # 儲存結果
            iu.save_image(output_path, fake_rgb_image)
            print(f"Processed and saved: {output_path}")
# 處理圖片
process_images(input_folder, output_folder)
