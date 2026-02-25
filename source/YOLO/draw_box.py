import cv2 as cv
import numpy as np

def draw_bounding_boxes():
    """
     검출된 객체의 영역을 표시
    """

    # 빈 이미지 생성
    img = np.ones((800,800,3), dtype=np.uint8) * 128
    
    # box 영역 좌표
    boxes = [
        {'bbox':(100,100,200,150), 'label': 'Person', 'confidencess':0.95},
        {'bbox':(400,100,150,180), 'label': 'Car', 'confidencess':0.87},
        {'bbox':(200,350,180,120), 'label': 'Dog', 'confidencess':0.92},
        {'bbox':(100,550,180,120), 'label': 'cat', 'confidencess':0.52}
    ]

    # 각각의 박스 영역 그리기
    for obj in boxes:
        x,y,w,h = obj['bbox']
        conf = obj['confidencess']
        label = obj['label']

        # 박스 그리기
        cv.rectangle(img, (x,y), (x+w,y+h), (255,255,0),1)

        text = f"{label}:{conf:.2f}"

        # 텍스트 배경 박스
        (text_width, text_height), _ = \
            cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        
        cv.rectangle(img, (x,y-text_height-10), 
                     (x+text_width,y), (0,255,0), -1)
        
        cv.putText(img, text, (x,y-5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0),2 )

    # 이미지 표시
    cv.imshow('Bounding box Example', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return img
    
# 실행
draw_bounding_boxes()
