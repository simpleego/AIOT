def calculate_iou(box1,box2):
    """
    두 bounding box의 IoU를 계산
    box 형식: (x, y, width, height)
    """
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    # 각 박스의 끝점 계산
    box1_x2 = x1 + w1
    box1_y2 = y1 + h1
    box2_x2 = x2 + w2
    box2_y2 = y2 + h2

    # 교집합 영역 계산
    inter_x1 = max(x1, x2)
    inter_y1 = max(y1, y2)
    inter_x2 = min(box1_x2, box2_x2)
    inter_y2 = min(box1_y2, box2_y2)

     # 교집합 면적
    inter_width = max(0, inter_x2 - inter_x1)
    inter_height = max(0, inter_y2 - inter_y1)
    intersection = inter_width * inter_height

    # 합집합 면적
    area1 = w1 * h1
    area2 = w2 * h2
    union = area1 + area2 - intersection

    # IoU 계산
    iou = intersection / union if union > 0 else 0
    
    print(f"Box1 면적: {area1}")
    print(f"Box2 면적: {area2}")
    print(f"교집합 면적: {intersection}")
    print(f"합집합 면적: {union}")
    print(f"IoU: {iou:.4f}")

    return iou

# 테스트
box1 = (150, 120, 190, 150)  # x, y, w, h
box2 = (150, 120, 200, 150)

iou = calculate_iou(box1, box2)