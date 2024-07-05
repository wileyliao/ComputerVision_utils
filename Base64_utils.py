import base64
import cv2
import numpy as np

def base64_encoder(image_path):
    with open(image_path, 'rb') as image_file:
        #轉換編碼
        base64_encoded_data = base64.b64encode(image_file.read())
        #編碼轉為字符串
        base64_encoded_str = base64_encoded_data.decode('utf-8')
    return base64_encoded_str

image = './ori_img/test003.jpg'
img_64 = base64_encoder(image)
print(img_64)

def base64_decoder(image_64):
    base64_string = image_64
    decode = base64.b64decode(base64_string)
    image_array = np.frombuffer(decode, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image

img_ori = base64_decoder(img_64)
cv2.imshow('Decoded Image', img_ori)
cv2.waitKey(0)  # 等待按鍵輸入
cv2.destroyAllWindows()  # 關閉所有 OpenCV 窗口