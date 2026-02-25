from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import os
from pathlib import Path

def batch_detection(image_folder, output_folder='output'):
    """
    폴더 내 모든 이미지에 대해 객체 검출 수행
    
    Args:
        image_folder: 이미지가 있는 폴더 경로
        output_folder: 결과를 저장할 폴더 경로
    """

    # 출력 폴더 생성
    Path(output_folder).mkdir(exist_ok=True)
    
    model = YOLO('yolov8n.pt')

    # 지원하는 이미지 확장자
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.webp']

    # 폴더 내 이미지 파일 찾기
    image_files = []
    for ext in image_extensions:
        image_files.extend(Path(image_folder).glob(f'*{ext}'))
    
    print(f"\n총 {len(image_files)}개 이미지 발견")
    print("=" * 60)

    results_summary = []

    for i in image_files:
        print(f"filename: {i}")

    for idx, image_path in enumerate(image_files, 1):
        print(f"\n[{idx}/{len(image_files)}] 처리 중: {image_path.name}")
        
        # 검출 수행
        results = model(str(image_path))
        
        # 검출된 객체 수
        num_detections = len(results[0].boxes)
        print(f"검출된 객체 수 : {num_detections}")

        # 결과 이미지 저장
        result_img = results[0].plot()
        output_path = os.path.join(output_folder, f'result_{image_path.name}')
        cv2.imwrite(output_path, result_img)

        # 통계 수집
        detected_classes = {}
        for box in results[0].boxes:
            cls_name = model.names[int(box.cls[0])]
            detected_classes[cls_name] = detected_classes.get(cls_name, 0) + 1
        
        results_summary.append({
            'file': image_path.name,
            'total': num_detections,
            'classes': detected_classes
        })
        
        print(f"  검출: {num_detections}개 - {detected_classes}")
    
    # 전체 요약
    print("\n" + "=" * 60)
    print("배치 처리 완료")
    print("=" * 60)
    
    for item in results_summary:
        print(f"\n{item['file']}: {item['total']}개")
        for cls_name, count in item['classes'].items():
            print(f"  - {cls_name}: {count}개")
    
    print(f"\n✓ 모든 결과가 '{output_folder}' 폴더에 저장되었습니다.")
    
    return results_summary

# 실행 예시
batch_detection('img', 'detection_results')
