import cv2
from matplotlib import pyplot as plt


def canny_threshold_checker(image_path, low_range, high_range, step=10):
    """
    根據Canny邊緣檢測的閾值範圍，顯示不同結果
    param:
        image_path: 圖片路徑
        low_range: 低閾值範圍
        high_range: 高閾值範圍
        step: 閾值的增量
    return:
        顯示不同閾值組合的邊緣檢測結果
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    plt.figure(figsize=(20, 20))
    plot_index = 1

    for low in range(low_range[0], low_range[1], step):
        for high in range(high_range[0], high_range[1], step):
            edges = cv2.Canny(image, low, high)
            plt.subplot((low_range[1] - low_range[0]) // step, (high_range[1] - high_range[0]) // step, plot_index)
            plt.imshow(edges, cmap='gray')
            plt.title(f'Low: {low}, High: {high}')
            plt.xticks([]), plt.yticks([])
            plot_index += 1

    plt.show()


# 檢查Canny邊緣檢測的閥值
image_path = './box_coord/metal01.jpg'
low_threshold_range = (0, 40)
high_threshold_range = (40, 100)

canny_threshold_checker(image_path, low_threshold_range, high_threshold_range)
