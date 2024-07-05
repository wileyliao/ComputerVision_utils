import cv2

def binarize_threshold_checker(img, start, end):
    """
    根據閥值範圍調整影像二值結果，並顯示圖片
    param
        img:圖片
        start: 起始threshold
        end: 終點threshold
    return:
        顯示每一次調整threshold圖片
    """
    for i, threshold_value in enumerate(range(start, end, 5), 1):
        _, img_bin = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
        cv2.imshow(f'{threshold_value}', img_bin)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#檢查閥值該設定多少
image_path = 'testtt.jpg'
img = cv2.imread(image_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
init, final = 140, 200
binarize_threshold_checker(img_gray, init,final)