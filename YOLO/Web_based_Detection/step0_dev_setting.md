# 전체 단계 로드맵(요약)

1. **1단계(오늘 제시)**: 웹캠 → 영상서버(수신/중계) → 웹서버(수신/화면표시)까지 “영상 파이프라인” 완성
2. 2단계: 웹서버에서 “버튼 클릭 → 현재 프레임 1장 추론 → JSON 반환 + 오버레이 이미지”
3. 3단계: 실시간 추론(프레임 스킵/리사이즈/비동기) + 다중 클라이언트 대응
4. 4단계: 운영형(큐/브로커, 다중 카메라, 인증, 저장, 장애복구)

---

# 1단계 목표(적당한 범위)

**목표:**

* “영상서버(ingest)”가 **웹캠 영상을 받아서**
* “웹서버(API)”가 **영상서버의 스트림을 받아서**
* 프론트(Svelte)가 **웹서버 스트림을 브라우저에서 재생**한다.

**핵심 포인트:**

* 영상서버는 “카메라 → 프레임 최신값 유지 → MJPEG로 배포”
* 웹서버는 “영상서버 MJPEG를 그대로 프록시(중계)”
  (1단계에서는 객체검출 X. 단, 다음 단계에서 여기 프레임을 바로 YOLO에 넣을 수 있게 구조를 잡음)

---

## 1단계 아키텍처

* **Cam Ingest Server (FastAPI #1, 예: 9001)**

  * 로컬 웹캠(OpenCV) 캡처
  * `/mjpeg` 로 MJPEG 스트림 제공

* **Web Server (FastAPI #2, 예: 8000)**

  * `/video`에서 ingest 서버의 MJPEG를 받아 그대로 중계
  * (추후 `/detect_once`, `/detect_stream` 같은 endpoint를 추가)

* **Frontend (Svelte, 예: 5173)**

  * `<img src="http://localhost:8000/video">` 로 실시간 표시

---

# 1단계 구현

## 0) 준비

```bash
pip install fastapi uvicorn opencv-python
```

---

## 1) 영상서버(웹캠 캡처 + MJPEG)

**cam_server.py**

```python
import cv2
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

cap = cv2.VideoCapture(0)  # 필요 시 1,2 또는 장치 인덱스 변경
if not cap.isOpened():
    raise RuntimeError("웹캠을 열 수 없습니다. 장치 인덱스를 확인하세요.")

def mjpeg_generator():
    # 간단한 FPS 제어(과부하 방지)
    target_fps = 15
    frame_interval = 1.0 / target_fps

    while True:
        t0 = time.time()
        ok, frame = cap.read()
        if not ok:
            time.sleep(0.1)
            continue

        # 필요 시 리사이즈(대역폭/CPU 절감)
        # frame = cv2.resize(frame, (640, 360))

        ok, jpg = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        if not ok:
            continue

        chunk = jpg.tobytes()
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + chunk + b"\r\n"
        )

        dt = time.time() - t0
        if dt < frame_interval:
            time.sleep(frame_interval - dt)

@app.get("/mjpeg")
def mjpeg():
    return StreamingResponse(
        mjpeg_generator(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )
```

실행:

```bash
uvicorn cam_server:app --host 0.0.0.0 --port 9001
```

브라우저에서 확인:

* `http://localhost:9001/mjpeg`

---

## 2) 웹서버(영상서버 스트림을 프록시)

**web_server.py**

```python
import requests
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

CAM_SERVER_MJPEG = "http://localhost:9001/mjpeg"

def proxy_stream():
    # stream=True로 MJPEG를 그대로 받아서 chunk 단위로 전달
    with requests.get(CAM_SERVER_MJPEG, stream=True, timeout=10) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

@app.get("/video")
def video():
    return StreamingResponse(
        proxy_stream(),
        media_type="multipart/x-mixed-replace; boundary=frame",
    )
```

실행:

```bash
pip install requests
uvicorn web_server:app --host 0.0.0.0 --port 8000
```

브라우저에서 확인:

* `http://localhost:8000/video`

---

## 3) 프론트엔드(Svelte)

Svelte에서 MJPEG는 보통 `<video>`보다 **`<img>`가 제일 간단**합니다.

**App.svelte**

```svelte
<script>
  const videoUrl = "http://localhost:8000/video";
</script>

<main style="padding:16px;">
  <h1>Live Video (MJPEG Proxy)</h1>
  <img
    src={videoUrl}
    alt="live"
    style="max-width: 100%; border: 1px solid #ccc; border-radius: 8px;"
  />
</main>
```

---

# 1단계 완료 기준(체크리스트)

* [ ] `localhost:9001/mjpeg`에서 웹캠 영상이 나온다
* [ ] `localhost:8000/video`에서 동일 영상이 나온다 (프록시 성공)
* [ ] Svelte 페이지에서 영상이 끊김 없이 나온다

---
