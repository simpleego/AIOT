# 📌 YOLO + DeepSORT 객체 추적 튜토리얼 (Python)

YOLO는 **객체 탐지**, DeepSORT는 **객체 추적(Tracking)**을 담당
두 기술을 결합하면 **사람·차량 등 객체를 ID 기반으로 지속적으로 추적**할 수 있음  

---

# 1️⃣ 필요한 라이브러리 설치

```bash
pip install opencv-python
pip install numpy
pip install filterpy
pip install scikit-learn
pip install lap
```

DeepSORT 구현체는 GitHub에서 가져오는 방식이 일반적이야.

---

# 2️⃣ DeepSORT GitHub 다운로드

```bash
git clone https://github.com/nwojke/deep_sort.git
```

구조는 다음과 같아:

```
deep_sort/
 ├── deep_sort/
 │     ├── detection.py
 │     ├── tracker.py
 │     ├── nn_matching.py
 │     ├── kalman_filter.py
 │     └── tools.py
 └── ...
```

---

# 3️⃣ YOLO + DeepSORT 통합 코드

아래 코드는 **YOLOv3 + OpenCV DNN + DeepSORT**를 결합한 예제야.

```python
import cv2
import numpy as np
from deep_sort.deep_sort import DeepSort

# YOLO 로드
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")
with open("yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# DeepSORT 초기화
deepsort = DeepSort(
    model_path="deep_sort/deep/checkpoint/ckpt.t7",
    max_dist=0.2,
    min_confidence=0.3,
    nms_max_overlap=0.5,
    max_iou_distance=0.7,
    max_age=70,
    n_init=3,
    nn_budget=100
)

# 웹캠 또는 영상 입력
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    # YOLO 입력 블롭 생성
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    boxes = []
    confidences = []
    class_ids = []

    # YOLO 탐지 결과 파싱
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                cx = int(detection[0] * width)
                cy = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(cx - w / 2)
                y = int(cy - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # DeepSORT 입력 형식 변환
    xywhs = []
    confs = []

    for i, box in enumerate(boxes):
        x, y, w, h = box
        xywhs.append([x + w/2, y + h/2, w, h])
        confs.append(confidences[i])

    xywhs = np.array(xywhs)
    confs = np.array(confs)

    # DeepSORT 추적 실행
    outputs = deepsort.update(xywhs, confs, frame)

    # 결과 표시
    for output in outputs:
        x1, y1, x2, y2, track_id = output
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("YOLO + DeepSORT Tracking", frame)

    if cv2.waitKey(1) == 27:  # ESC 종료
        break

cap.release()
cv2.destroyAllWindows()
```

---

# 4️⃣ 동작 방식 요약

| 기술 | 역할 |
|------|------|
| **YOLO** | 객체 탐지 (bounding box 생성) |
| **DeepSORT** | Kalman Filter + ReID 모델로 객체 추적 |
| **결과** | 객체마다 고유 ID 부여 → 지속 추적 가능 |

---

# 5️⃣ 결과 화면 예시

- 사람 1 → ID 3  
- 사람 2 → ID 7  
- 차량 1 → ID 12  

프레임이 바뀌어도 같은 객체는 같은 ID로 추적돼.

---

# 6️⃣ 확장 아이디어

- CCTV 영상에서 **사람 수 카운팅**
- 특정 영역 침입 감지(ROI 기반)
- 차량 번호판 인식과 결합
- YOLOv8 + DeepSORT로 업그레이드
- 웹캠 기반 실시간 경고 시스템

---
