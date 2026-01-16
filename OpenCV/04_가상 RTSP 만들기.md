# 가상 RTSP 만들기

## 1️⃣ 가장 간단한 방법: RTSP처럼 쓰는 추상화 레이어 만들기

실제로는 **동영상 파일**을 읽으면서, 코드 상에서는 `rtsp_url`을 쓰는 것처럼 보이게 만드는 방식이야.

```python
import cv2

class VirtualRTSP:
    def __init__(self, source):
        # source: 동영상 파일 경로 또는 웹캠 번호
        self.cap = cv2.VideoCapture(source)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()

# 실제 RTSP 대신 가상 RTSP 사용
# rtsp_url = "rtsp://..."  # 실제 CCTV라면 이렇게
rtsp_url = "cctv_sample.mp4"  # 가상 RTSP: 동영상 파일

stream = VirtualRTSP(rtsp_url)

while True:
    ret, frame = stream.read()
    if not ret:
        break

    # 여기서 YOLO/DeepSORT/CCTV 분석 로직 수행
    cv2.imshow("Virtual RTSP Stream", frame)

    if cv2.waitKey(1) == 27:
        break

stream.release()
cv2.destroyAllWindows()
```

이렇게 해두면 나중에 **실제 RTSP URL만 넣어도 코드 전체를 바꿀 필요가 없어**.

---

## 2️⃣ 진짜 RTSP 서버처럼 만들기 (ffmpeg + 로컬 RTSP 서버)

조금 더 리얼하게 가고 싶다면, **동영상 파일 → RTSP 스트림으로 송출**해서  
정말 `rtsp://...` 주소를 사용하는 방식도 있어.

### 2-1. rtsp-simple-server 설치 (예: mediamtx)

1. GitHub에서 `mediamtx`(구 rtsp-simple-server) 다운로드  
2. 실행:

```bash
./mediamtx
```

기본 RTSP 포트 8554로 서버가 떠.

### 2-2. ffmpeg로 동영상 → RTSP로 송출

```bash
ffmpeg -re -stream_loop -1 -i cctv_sample.mp4 -c copy -f rtsp rtsp://localhost:8554/test
```

이제 아래처럼 코드에서 진짜 RTSP처럼 사용할 수 있어:

```python
import cv2

rtsp_url = "rtsp://localhost:8554/test"
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 여기서 YOLO/DeepSORT/CCTV 분석 로직 수행
    cv2.imshow("RTSP Stream", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 3️⃣ 기존 CCTV 분석 코드에 자연스럽게 녹이는 방법

앞에서 만들었던 CCTV 분석 코드에서 이 부분만 바꾸면 돼:

```python
# 기존
# video_path = "cctv_sample.mp4"
# cap = cv2.VideoCapture(video_path)

# 가상 RTSP 버전
rtsp_url = "cctv_sample.mp4"  # 나중에 실제 RTSP로 교체 가능
cap = cv2.VideoCapture(rtsp_url)
```

혹은 아예 이렇게 추상화해두면 더 깔끔하고:

```python
def open_stream(source):
    return cv2.VideoCapture(source)

# 가상 RTSP
stream = open_stream("cctv_sample.mp4")

# 실제 RTSP
# stream = open_stream("rtsp://user:pass@ip:port/Streaming/Channels/101")
```

---
