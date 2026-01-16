# 📌 CCTV 영상 자동 분석 시스템 개요

**목표:**  
- CCTV 영상에서  
  - 사람/차량 탐지  
  - 침입 감지(관심 구역 진입)  
  - 인원 수 카운팅  
  - 로그/이벤트 저장  

**구성 요소:**  
- 입력: CCTV RTSP 스트림 또는 동영상 파일  
- 분석: YOLO(+선택적으로 DeepSORT)  
- 로직: 침입 감지, 카운팅, 체류 시간 등  
- 출력: 화면 표시 + 로그 파일 저장(또는 DB)

---

## 1️⃣ 기본 환경 세팅

```bash
pip install opencv-python
pip install numpy
pip install ultralytics   # YOLOv8 기준 (추천)
```

---

## 2️⃣ YOLOv8 기반 CCTV 분석 기본 코드

```python
import cv2
from ultralytics import YOLO
import datetime

# YOLO 모델 로드 (사전 학습된 COCO 모델)
model = YOLO("yolov8n.pt")  # 가볍고 빠른 버전

# CCTV RTSP 또는 동영상 파일
# rtsp_url = "rtsp://user:pass@ip:port/Streaming/Channels/101"
video_path = "cctv_sample.mp4"
cap = cv2.VideoCapture(video_path)

# 관심 구역(ROI) 설정 예시 (x1, y1, x2, y2)
ROI = (200, 100, 800, 600)

def is_in_roi(x1, y1, x2, y2, roi):
    rx1, ry1, rx2, ry2 = roi
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return rx1 <= cx <= rx2 and ry1 <= cy <= ry2

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO 추론
    results = model(frame, imgsz=640, conf=0.5)

    person_count = 0
    intrusion_events = []

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cls = int(box.cls[0].cpu().numpy())
            conf = float(box.conf[0].cpu().numpy())

            # COCO 기준 0: person, 2: car, 3: motorcycle, 5: bus, 7: truck 등
            if cls == 0:  # 사람만 분석
                person_count += 1

                in_roi = is_in_roi(x1, y1, x2, y2, ROI)

                color = (0, 255, 0) if not in_roi else (0, 0, 255)
                label = f"Person {conf:.2f}"

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

                if in_roi:
                    intrusion_events.append((x1, y1, x2, y2))

    # ROI 영역 표시
    rx1, ry1, rx2, ry2 = ROI
    cv2.rectangle(frame, (rx1, ry1), (rx2, ry2), (255, 0, 0), 2)
    cv2.putText(frame, "ROI", (rx1, ry1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # 화면 상단에 인원 수 표시
    cv2.putText(frame, f"Person Count: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

    # 침입 이벤트가 있으면 로그 출력 (파일로도 저장 가능)
    if intrusion_events:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Intrusion detected! Count: {len(intrusion_events)}")

    cv2.imshow("CCTV Analysis", frame)

    if cv2.waitKey(1) == 27:  # ESC 종료
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 3️⃣ 기능별 설명

- **관심 구역(ROI) 기반 침입 감지**
  - 사각형 영역 안에 사람의 중심점이 들어오면 “침입”으로 판단
- **인원 수 카운팅**
  - 프레임 단위로 사람 수를 세고 화면에 표시
  - 원하면 “라인 크로싱” 방식으로 출입 인원 카운팅도 가능
- **이벤트 로그**
  - 침입 발생 시 시간 + 이벤트 내용을 파일/DB에 기록 가능

---

## 4️⃣ 로그 파일로 저장 예시

```python
import csv

log_file = "intrusion_log.csv"

# 최초 1회 헤더 작성
with open(log_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "event", "count"])

# 침입 발생 시
if intrusion_events:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([now, "intrusion", len(intrusion_events)])
```

---

## 5️⃣ 확장 아이디어

- **DeepSORT 추가**:  
  - 사람마다 ID를 부여해서 “얼마나 오래 머물렀는지”, “어디서 어디로 이동했는지” 추적
- **웹 대시보드 연동**:  
  - Flask/FastAPI + 웹소켓으로 실시간 화면/이벤트 전송
- **알림 시스템**:  
  - 특정 시간대 침입 시 Slack/카카오톡/메일 알림
- **다중 CCTV 관리**:  
  - 여러 RTSP 스트림을 스레드/프로세스로 병렬 처리

---
