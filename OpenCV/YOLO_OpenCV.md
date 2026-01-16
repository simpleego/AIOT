# 📌 YOLO + OpenCV 연동 튜토리얼 (Python)  

---

## 1️⃣ 준비물 다운로드

### ✔ YOLOv3 모델 파일 3종  
- `yolov3.weights`  
- `yolov3.cfg`  
- `coco.names`

다운로드 링크:  
https://pjreddie.com/darknet/yolo/

---

## 2️⃣ 파이썬 환경 준비

```bash
pip install opencv-python
pip install numpy
```

---

## 3️⃣ 프로젝트 구조

```
project/
 ├── yolo/
 │    ├── yolov3.cfg
 │    ├── yolov3.weights
 │    └── coco.names
 └── detect.py
```

---

## 4️⃣ YOLO + OpenCV 연동 코드 (detect.py)

```python
import cv2
import numpy as np

# YOLO 모델 로드
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")

# COCO 클래스 이름 로드
with open("yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 출력 레이어 이름 가져오기
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# 이미지 로드
img = cv2.imread("test.jpg")
height, width, channels = img.shape

# YOLO 입력 블롭 생성
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# 추론 실행
outs = net.forward(output_layers)

# 결과 분석
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# NMS(중복 박스 제거)
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# 결과 그리기
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = (0, 255, 0)

        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# 결과 출력
cv2.imshow("YOLO Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 5️⃣ 실행 방법

```bash
python detect.py
```

---

## 6️⃣ 웹캠 실시간 YOLO 적용 코드

```python
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    height, width, _ = frame.shape
    boxes = []
    confidences = []
    class_ids = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = (0, 255, 0)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("YOLO Webcam", frame)

    if cv2.waitKey(1) == 27:  # ESC 종료
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 7️⃣ YOLOv5 / YOLOv8로 확장하는 방법

YOLOv5·v8은 PyTorch 기반이라 아래처럼 사용해.

```python
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("image.jpg")
```

---
