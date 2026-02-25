def filter_by_confidence(detectios, threshold=0.5):
    """
    Confidence Score가 임계값 이상인 검출 결과만 필터링
    """
    # 예시 검출 결과
    sample_detections = [
        {'class': 'person', 'confidence': 0.95, 'bbox': (100, 100, 50, 100)},
        {'class': 'car', 'confidence': 0.42, 'bbox': (200, 150, 80, 60)},
        {'class': 'dog', 'confidence': 0.88, 'bbox': (300, 200, 60, 70)},
        {'class': 'person', 'confidence': 0.35, 'bbox': (400, 250, 45, 95)},
    ]

    filtered = [d for d in sample_detections if d['confidence'] >= threshold]
    
    print(f"전체 검출 수: {len(sample_detections)}")
    print(f"임계값 {threshold} 이상 검출 수: {len(filtered)}")
    print("\n필터링된 결과:")
    for det in filtered:
        print(f"  - {det['class']}: {det['confidence']:.2f}")
    
    return filtered

# 테스트
filtered_results = filter_by_confidence([], threshold=0.4)