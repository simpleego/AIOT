import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 읽기
def load_and_display_image(image_path):
    """
    이미지를 읽고 화면에 표시한다.
    """
    #이미지 읽기(BGR 형식)
    img = cv2.imread(image_path)

    if img is None:
        print("이미지를 찾을 수 없습니다.")
        return None
    
    # 이미지 변환
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 이미지 정보 출력
    print(f"이미지 크기:{img.size}")
    print(f"이미지 너비:{img.shape[1]}")
    print(f"이미지 높이:{img.shape[0]}")
    print(f"이미지 채널:{img.shape[2]}")

    # 이미지 표시
    plt.figure(figsize=(10,6))
    plt.subplot(1, 2, 1)   # 1행 2열 중 첫 번째
    plt.imshow(img_rgb)
    plt.title('cat 1')
    plt.axis('off')

    plt.subplot(1, 2, 2)   # 1행 2열 중 두 번째
    plt.imshow(img_rgb)
    plt.title('cat 2')
    plt.axis('on')

    plt.tight_layout()
    plt.show()

    return img


img = load_and_display_image('img/cat1.jpg')