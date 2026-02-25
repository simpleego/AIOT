from ultralytics import YOLO
import cv2

def test_yolo_installation():
    """
    YOLO가 정상적으로 설치되었는지 확인
    """
    try:
        # YOLOv8 nano 모델 로드 (가장 가벼운 모델)
        print("YOLO 모델 로딩 중...")
        model = YOLO('yolov8n.pt')
        
        print("✓ YOLO 설치 성공!")
        print(f"모델 정보: {model.model}")
        print(f"지원 클래스 수: {len(model.names)}")
        
        # 클래스 이름 일부 출력
        print("\n지원 클래스 예시 (처음 10개):")
        for i, name in list(model.names.items())[:10]:
            print(f"  {i}: {name}")
        
        return model
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")
        return None

# 실행
model = test_yolo_installation()