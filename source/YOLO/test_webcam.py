import cv2

def test_webcam():
    """
    웹캡 동작 테스트
    q를 누르면 종료하도록 설정
    """
    # 웹캡 열기(0은 기본 카메라)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("웹갬을 열 수 없습니다.")
        return
    
    print("웹갭을 테스트 합니다.종료는 q")

    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        cv2.putText(frame, 'Press Q to Quit', (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,00),2)
        
        # 프레임 표시
        cv2.imshow('Webcam Test', frame)

        # 종료 처리
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 리소스 해제

    cap.release()
    cv2.destroyAllWindows()

test_webcam()