import cv2

# 讀取圖片
image = cv2.imread(r"C:\database\hw_num\png_file\output_page_15.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化（Thresholding）
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# 找輪廓
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

counter = 0

# 遍歷所有輪廓，篩選方形框
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    # 篩選出四邊形
    if len(approx) == 4 and cv2.isContourConvex(approx):
        x, y, w, h = cv2.boundingRect(approx)

        # 根據長寬比篩選接近正方形或矩形的框
        aspect_ratio = float(w) / h
        if 0.8 < aspect_ratio < 1.2:  # 這裡篩選接近正方形的框
            cropped_img = image[y:y+h, x:x+w]
            filename = f"cropped_{x}_{y}.png"
            cv2.imwrite(filename, cropped_img)
            print(f"Saved: {filename}")
            counter += 1


            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)  # 用綠色標註
print(counter)

# 顯示結果
# cv2.imshow("Detected Squares", image)
# cv2.imwrite('test03.png', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
