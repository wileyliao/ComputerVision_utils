import cv2

class RectangleDrawer:
    def __init__(self, image_path, scale=1.0):
        self.image_path = image_path
        self.scale = scale
        self.img = cv2.imread(image_path)

        if self.img is None:
            raise ValueError(f"Failed to load image from {image_path}")

        # 調整圖片大小
        self.img = cv2.resize(self.img, (0, 0), fx=self.scale, fy=self.scale)
        self.original_img = cv2.imread(image_path)  # 保留原始大小的圖片，用於裁剪
        self.rect = []
        self.drawing = False
        self.crop_counter = 0  # 用於裁剪檔名編號

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # 滑鼠按下左鍵
            self.rect = [(x, y)]  # 紀錄起始位置
            self.drawing = True
        elif event == cv2.EVENT_MOUSEMOVE:  # 滑鼠移動
            if self.drawing:
                img_copy = self.img.copy()
                cv2.rectangle(img_copy, self.rect[0], (x, y), (0, 255, 0), 2)
                cv2.imshow("image", img_copy)
        elif event == cv2.EVENT_LBUTTONUP:  # 滑鼠鬆開左鍵
            self.rect.append((x, y))  # 紀錄終止點
            self.drawing = False
            cv2.rectangle(self.img, self.rect[0], self.rect[1], (0, 255, 0), 2)
            cv2.imshow("image", self.img)

            # 把座標轉回原始圖片比例
            rect_original = [(int(p[0] / self.scale), int(p[1] / self.scale)) for p in self.rect]
            print(f"Selected Rectangle Coordinates (scaled back to original): {rect_original}")

            # 裁剪原始圖片範圍並存成檔案
            self.crop_and_save(rect_original)

    def crop_and_save(self, rect):
        """根據原始圖片座標裁剪並存成檔案"""
        x1, y1 = rect[0]
        x2, y2 = rect[1]

        # 確保座標正確，防止負值或反向座標
        x1, x2 = sorted([max(0, x1), max(0, x2)])
        y1, y2 = sorted([max(0, y1), max(0, y2)])

        cropped_img = self.original_img[y1:y2, x1:x2]

        if cropped_img.size > 0:
            file_name = f"cropped_image_{self.crop_counter}.png"
            cv2.imwrite(file_name, cropped_img)
            self.crop_counter += 1
            print(f"Cropped image saved as {file_name}")
        else:
            print("Invalid crop region, no image saved.")

    def start_drawing(self):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.draw_rectangle)

        while True:
            cv2.imshow("image", self.img)
            if cv2.waitKey(1) & 0xFF == 27:  # 按下 ESC 退出
                break
        cv2.destroyAllWindows()


# 使用示例
if __name__ == "__main__":
    # scale 可設定放大或縮小倍數，例如 0.5 表示縮小為原來的一半，2 表示放大兩倍
    drawer = RectangleDrawer(
        r"C:\database\hw_num\png_file\output_page_19.png",
        scale=0.2
    )
    drawer.start_drawing()
