# 🎬 1단계: 동영상 파일을 “가상의 RTSP 스트림”처럼 사용하는 구조
> 지금 단계에서는 **실제 CCTV 없이도 ‘RTSP처럼’ 동작하는 개발 환경**을 만드는 게 핵심
> 즉, **동영상 파일을 RTSP 스트림처럼 취급**해서 YOLO·DeepSORT·CCTV 분석 코드를 그대로 테스트할 수 있게 만드는 구조 생성
> 실제 RTSP URL 대신 **동영상 파일 경로를 넣어도 동일하게 동작**하도록 추상화 레이어를 생성  

---

## 🟩 1) VirtualRTSP 클래스 만들기

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
```

이제 이 클래스는 **RTSP처럼 read()로 프레임을 가져오는 역할**을 해.

---

## 🟦 2) 가상 RTSP 스트림 열기

```python
# 실제 RTSP라면:
# rtsp_url = "rtsp://user:pass@ip:port/Streaming/Channels/101"

# 1단계: 동영상 파일을 가상 RTSP처럼 사용
rtsp_url = "cctv_sample.mp4"

stream = VirtualRTSP(rtsp_url)
```

---

## 🟨 3) 프레임 읽기 + 화면 출력 테스트

```python
while True:
    ret, frame = stream.read()
    if not ret:
        break

    cv2.imshow("Virtual RTSP Stream", frame)

    if cv2.waitKey(1) == 27:  # ESC 종료
        break

stream.release()
cv2.destroyAllWindows()
```

이렇게 하면 **동영상 파일이 RTSP처럼 동작**하고,  
나중에 실제 CCTV RTSP URL만 넣으면 전체 코드가 그대로 작동해.

---

# 🧩 4) YOLO/DeepSORT 분석 코드와 결합하는 방법

기존 CCTV 분석 코드에서 이 부분만 바꾸면 돼:

```python
# 기존
# cap = cv2.VideoCapture("cctv_sample.mp4")

# 변경
stream = VirtualRTSP("cctv_sample.mp4")
```

그리고 프레임 읽는 부분도:

```python
ret, frame = stream.read()
```

이렇게 하면 YOLO, DeepSORT, ROI 침입 감지 등  
**전체 CCTV 분석 시스템을 실제 RTSP 없이 개발·디버깅 가능**해.

---
