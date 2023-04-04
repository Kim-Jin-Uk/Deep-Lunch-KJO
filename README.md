# Deep-Lunch-KJO
 딥런치 스터디 관련 소스
# 7주차 프로젝트 논의
## 프레임 워크

> PyTorch, TensorFlow > js로 개발한다면 TensorFlow 아니면 PyTorch, 

### 모델 구현 가능성
- 거의 모든 딥러닝 알고리즘을 구현할 수 있다
- 선택한 알고리즘을 구현하는 데 제약이 없다

### 높은 성능
- 하드웨어 최적화로 대규모 딥러닝 모델 학습 및 추론에 높은 성능을 보인다

### 커뮤니티
- 큰 개발자 커뮤니티를 보유
- 다양한 예제 코드, 라이브러리, 툴킷 등이 공유

## 알고리즘
### CNN
- CNN은 이미지와 같은 2D 데이터에서 탁월한 성능
- 이미지의 특징을 추출하기 위해 합성곱(Convolution) 연산을 사용
- 이미지의 로컬한 특징을 추출, 이미지를 분류

> 데이터 증강(data augmentation)을 통해 데이터의 다양성을 높임
> 전이학습(transfer learning)을 사용하여 미리 학습된 모델을 활용

## 데이터 셋

### 해외 지폐
https://www.kaggle.com/search?q=banknote+datasetFileTypes%3Ajpg+datasetFileTypes%3Apng

### 한국 지폐 (구권임..)
https://www.kogl.or.kr/search/search.do?query=%EC%A7%80%ED%8F%90

> 구글링 해야하지 않을까
