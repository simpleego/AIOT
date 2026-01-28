# OpenCV 영상처리 함수
> 영상 입출력, 기초 처리, 필터링, 변환, 특징 추출, 분할 등 다양한 영상처리 함수를 제공합니다.
> 모든 함수를 한 번에 나열하기는 방대하지만, 주요 기능별로 분류하면 체계적으로 정리**  

---

## 📌 OpenCV 주요 영상처리 함수 분류

### 1. 영상 입출력
- **imread()** : 이미지 파일 읽기  
- **imwrite()** : 이미지 파일 저장  
- **imshow()** : 이미지 출력  
- **VideoCapture()** : 카메라/동영상 입력  
- **VideoWriter()** : 동영상 저장  

---

### 2. 색상 및 채널 처리
- **cvtColor()** : 색 공간 변환 (BGR ↔ Gray, HSV 등)  
- **split() / merge()** : 채널 분리 및 합성  
- **inRange()** : 특정 색상 범위 마스크 추출  

---

### 3. 기초 영상 처리
- **resize()** : 크기 변경  
- **flip()** : 상하/좌우 반전  
- **rotate()** : 회전  
- **copyMakeBorder()** : 테두리 추가  

---

### 4. 필터링 및 블러링
- **blur() / boxFilter()** : 평균 블러  
- **GaussianBlur()** : 가우시안 블러  
- **medianBlur()** : 중앙값 필터  
- **bilateralFilter()** : 양방향 필터 (노이즈 제거 + 경계 유지)  

---

### 5. 에지 검출 및 특징 추출
- **Canny()** : 에지 검출  
- **Sobel() / Scharr()** : 방향성 에지 검출  
- **Laplacian()** : 라플라시안 에지 검출  
- **cornerHarris() / goodFeaturesToTrack()** : 코너 검출  
- **HoughLines() / HoughCircles()** : 직선/원 검출  

---

### 6. 영상 분할 및 임계값 처리
- **threshold()** : 단순 임계값 이진화  
- **adaptiveThreshold()** : 적응형 임계값  
- **watershed()** : 워터셰드 알고리즘  
- **grabCut()** : 전경/배경 분할  

---

### 7. 형태학적 연산
- **erode()** : 침식  
- **dilate()** : 팽창  
- **morphologyEx()** : 열림, 닫힘, 그라디언트, 탑햇, 블랙햇  

---

### 8. 기하학적 변환
- **warpAffine()** : 아핀 변환 (이동, 회전, 스케일)  
- **warpPerspective()** : 투시 변환  
- **getRotationMatrix2D()** : 회전 행렬 생성  
- **getPerspectiveTransform()** : 투시 변환 행렬 생성  

---

### 9. 그리기 함수
- **line()** : 직선 그리기  
- **rectangle()** : 사각형 그리기  
- **circle()** : 원 그리기  
- **ellipse()** : 타원 그리기  
- **putText()** : 문자열 출력  

---

### 10. 고급 영상 처리
- **pyrDown() / pyrUp()** : 이미지 피라미드  
- **remap()** : 좌표 매핑  
- **equalizeHist()** : 히스토그램 평활화  
- **calcHist()** : 히스토그램 계산  
- **matchTemplate()** : 템플릿 매칭  
- **findContours() / drawContours()** : 윤곽선 검출 및 그리기  

---
