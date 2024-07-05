import cv2

def roi_cutter(image, coords):
    """
    將座標對應圖片中位置裁剪
    param:
        image: 圖片
        coords: 欲裁剪BOX的座標
    return:
        裁剪後的圖片
    """
    (x1, y1), (x2, y2) = coords
    top_left_x = min(x1, x2)
    top_left_y = min(y1, y2)
    bottom_right_x = max(x1, x2)
    bottom_right_y = max(y1, y2)
    roi_image = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    return roi_image

def roi_checker(folder_path, box_coords):
    """
    檢查roi在每張圖片標記的結果
    param:
        folder_path: 輸入資料夾路徑
        box_coords: 座標[(x1, y1), (x2, y2)]，表示 Box 的左上和右下角
    return:
        顯示每一張標記好box的圖片
    """

    box_coords = sorted(box_coords)

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)
        # 在圖上標記 box1
        cv2.rectangle(image, box_coords[0], box_coords[1], (0, 255, 0), 2)
        cv2.imshow('Image with Boxes', image)

        # 按下 'q' 退出
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# box_coords = [(10, 315), (906, 455)]
# folder_path = './test'
# roi_checker(folder_path, box_coords)

def roi_saver(folder_path,output_folder_box1, output_folder_box2, box1_coords, box2_coords):
    """
    將圖片標記的box(此為兩個boxes)裁剪下來並分別存至對應名稱的資料夾
    param
        folder_path: 輸入資料路徑
        output_folder_box1: box1的存檔路徑
        output_folder_box2: box2的存檔路徑
        box1_coords: 座標[(x1, y1), (x2, y2)]，表示 Box1 的左上和右下角
        box2_coords: 座標[(x1, y1), (x2, y2)]，表示 Box2 的左上和右下角
    return:
        寫入每一張圖片至對應資料夾
    """
    box1_coords = sorted(box1_coords)
    box2_coords = sorted(box2_coords)

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image = cv2.imread(image_path)

        x1, y1 = box1_coords[0]
        x2, y2 = box1_coords[1]
        box1_crop = image[y1:y2, x1:x2]
        box1_save_path = os.path.join(output_folder_box1, f"{os.path.splitext(image_file)[0]}_box1.jpg")
        cv2.imwrite(box1_save_path, box1_crop)

        # 裁剪 box2 区域
        x1, y1 = box2_coords[0]
        x2, y2 = box2_coords[1]
        box2_crop = image[y1:y2, x1:x2]
        box2_save_path = os.path.join(output_folder_box2, f"{os.path.splitext(image_file)[0]}_box2.jpg")
        cv2.imwrite(box2_save_path, box2_crop)

# box1_coord = [(264, 154), (5, 5)]
# box2_coord = [(4, 375), (955, 500)]
# folder_path = './test'
# #建立資料存檔路徑
# output_folder_box1 = 'box1_coord'
# output_folder_box2 = 'box2_coord'
# os.makedirs(output_folder_box1, exist_ok=True)
# os.makedirs(output_folder_box2, exist_ok=True)
# roi_save(folder_path,output_folder_box1, output_folder_box2, box1_coords, box2_coords)

