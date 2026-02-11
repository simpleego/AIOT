import cv2 as cv

# 영상로드
video_path = "mov/beach.mp4"
capture = cv.VideoCapture(video_path)

if not capture.isOpened():
    print("영상을 열 수 없습니다..")
    exit()

# 1. 모든 프레임을 리스트에 저장
print("영상을 읽어오는 중....")
frames = []  # 영상 rewind(되감기)
fps = capture.get(cv.CAP_PROP_FPS)
if fps == 0: fps = 30

while True:
    ret, frame = capture.read()
    if not ret: break
    frames.append(frame)

capture.release()
total_frames = len(frames)

#2. 제어 변수(역방향 재생)
idx = 0
direction = 1 # 재생 방향
speed_multiplier = 1 # 속도 제어

while True:
    display_frame = frames[int(idx)].copy()

    # 상태 표시
    status = f"Speed: {speed_multiplier}x | {'Reverse' if direction == -1 else 'Forward'}"
    cv.putText(display_frame, status, (10,30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
    cv.imshow("VideoFrame", display_frame)

    idx = (idx + (direction * speed_multiplier)) % total_frames

    key = cv.waitKeyEx(max(1, int(1000 / (fps*1))))  # 속도 체감을 위해서 대기 시간 고정
    #key = cv.waitKeyEx(30) 

    if key == 27:  # ESC
        break
    elif key == 8: # backspace
        direction = -1
    elif key == 32: # space bar
        direction = 1
    elif key in [2621440, 84, 1]: # down key
        speed_multiplier = max(1,speed_multiplier -1)
        print(f"속도 감소 : {speed_multiplier}x")
    elif key in [2490368, 82, 0]: # down key
        speed_multiplier += 1
        print(f"속도 증가 : {speed_multiplier}x")   


cv.destroyAllWindows()