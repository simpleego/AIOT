# 📌 가상 RTSP + YOLO 분석 통합 코드 (완성본)
> **가상 RTSP 환경(VirtualRTSP)**을 그대로 활용해서  
> **YOLO 분석 코드와 완전히 연결된 형태**생성
> 아래 코드는 **1) 가상 RTSP → 2) YOLO 분석 → 3) 화면 출력**까지 한 번에 동작

```python
import cv2
from ultralytics import YOLO

# -----------------------------
# 1. 가상 RTSP 클래스 정의
# -----------------------------
class VirtualRTSP:
    def __init__(self, source):
        # source: 동영상 파일 경로 또는 웹캠 번호
        self.cap = cv2.VideoCapture(source)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()


# -----------------------------
# 2. YOLO 모델 로드
# -----------------------------
model = YOLO("yolov8n.pt")  # 가볍고 빠른 YOLOv8 nano 모델


# -----------------------------
# 3. 가상 RTSP 스트림 열기
# -----------------------------
# 실제 RTSP라면:
# rtsp_url = "rtsp://user:pass@ip:port/Streaming/Channels/101"

# 1단계: 동영상 파일을 RTSP처럼 사용
rtsp_url = "cctv_sample.mp4"
stream = VirtualRTSP(rtsp_url)


# -----------------------------
# 4. 프레임 반복 처리
# -----------------------------
while True:
    ret, frame = stream.read()
    if not ret:
        print("스트림 종료")
        break

    # YOLO 추론
    results = model(frame, imgsz=640, conf=0.5)

    # 탐지 결과 그리기
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cls = int(box.cls[0].cpu().numpy())
            conf = float(box.conf[0].cpu().numpy())
            label = f"{model.names[cls]} {conf:.2f}"

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),
                          (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 화면 출력
    cv2.imshow("Virtual RTSP + YOLO Detection", frame)

    if cv2.waitKey(1) == 27:  # ESC 종료
        break

stream.release()
cv2.destroyAllWindows()
```

---

# 🎯 이 코드가 해주는 일

### ✔ 1) 동영상 파일을 RTSP처럼 취급  
- `VirtualRTSP("cctv_sample.mp4")`  
- 실제 RTSP URL로 바꿔도 코드 전체 수정 필요 없음

### ✔ 2) YOLOv8으로 객체 탐지  
- 사람, 차량, 동물 등 COCO 데이터셋 기반 탐지  
- bounding box + confidence 표시

### ✔ 3) 실시간 CCTV 분석처럼 동작  
- 프레임 단위로 YOLO 분석  
- ESC로 종료

---

# 🚀 다음 단계로 확장 가능

원하면 아래 기능도 바로 붙여줄 수 있어:

- DeepSORT 추가 → **객체 추적 + ID 부여**
- ROI 침입 감지 기능 추가
- 인원 수 카운팅 기능 추가
- 이벤트 로그 저장 기능 추가
- 여러 개 가상 RTSP 스트림 동시 처리
- Flask 웹 대시보드로 실시간 스트리밍
