"""
1단계 종합 실습: 기본 환경 설정 확인 프로그램
"""
import cv2
import numpy as np
from ultralytics import YOLO
import sys

class YOLOSetupChecker:
    """
        YOLO 학습 환경 설정을 확인하는 클래스
    """
    def __init__(self):
        self.results = {}

    def check_opencv(self):
        """ OpenCV 설치 확인 """
        try:
            version = cv2.__version__
            self.results['opencv'] = f"openCV{version} 설치됨"
            return True
        except:
            self.results['opencv'] = "OpenCV 설치 필요"
            return False
        
    def check_numpy(self):
        """ numpy 설치 확인 """
        try:
            version = np.__version__
            self.results['numpy'] = f"numpy{version} 설치됨"
            return True
        except:
            self.results['numpy'] = "numpy 설치 필요"
            return False
        
    def check_yolo(self):
        """ YOLO 설치 확인 """
        try:
            model = YOLO('yolov8n.pt')
            self.results['yolo'] = f"YOLO  모델 로드 성공"
            return True
        except Exception as e:
            self.results['yolo'] = f"YOLO 오류 {str(e)}"
            return False
        
    def check_webcam(self):
        """ 웹캠 접근 확인 """
        try:
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                ret, frame = cap.read()
                cap.release()
                if ret:
                    self.results['webcam'] = "웹캠 정상 동작"
                    return True
                
            self.results['webcam'] = " 웹캠 접근 불가"
            return False
        except:
            self.results['webcam'] = " 웹캠 오류"
        
    def run_all_check(self):
        """ 모든 체크 실행 """
        print("="*50)
        print("YOLO 학습 환경 설정 확인")
        print("="*50)

        self.check_opencv()
        self.check_numpy()
        self.check_yolo()
        self.check_webcam()

        print("\n 결과 출력 ")
        for key, value in self.results.items():
            print(f"{value}")

## 
if __name__ == "__main__":
    checker = YOLOSetupChecker()
    checker.run_all_check()
    
