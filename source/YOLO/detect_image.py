from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

def simple_image_detection(image_path):
    """
    이미지에서 객체 검출 수행
    """
    # 모델 로드
    model = YOLO('yolov8n.pt')

    # 이미지 읽기
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 객체 검출
    results = model(image_path)

    # 결과 시각화
    result_img = results[0].plot()
    result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

    # 원본과 결과 비교
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    axes[0].imshow(img_rgb)
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    axes[1].imshow(result_img_rgb)
    axes[1].set_title('Detection Result')
    axes[1].axis('off')
    
    plt.tight_layout()
    plt.show()

    # 검출된 객체 정보 출력
    print("\n검출된 객체:")
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            print(f"  - {model.names[cls]}: {conf:.2f}")

simple_image_detection('img/bus.jpg')
    