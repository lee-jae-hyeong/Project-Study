# 개인프로젝트
### 1. 주제 : Amazon Reviews 데이터를 활용한 NLP 추천 모델링 구현
### 2. 프로젝트 기간 : Version1 (2021.06.01 ~ 2021.06.11) / Version2(추가 보완)
#
### 3. 주제 선정 이유 
#### - 이커머스나 OTT 등 추천 시스템은 매우 필수적인 요소가 되었기 때문에 아이템 기반의 협업 필터링 구현을 통해 사용자들에게 추천을 하기 위함.
#### - 아이템 기반 협업 필터링의 경우, 콜드 스타트 문제가 있어서 신규 고객이나 고객 행동 패턴이 거의 없을 경우에 적용하기엔 한계가 있음. 
#### - 내용 기반 추천 알고리즘과는 다른 새로운 추천 방식을 적용해보고자 NLP를 활용하여 추천 시스템을 구현하기 위함
#  
### 4. 데이터 : Amazon Reviews Data 
#### - Feature data : train_data(40000 x 10), test_data(10000 x 10)
#### - URL : https://www.kaggle.com/kashnitsky/hierarchical-text-classification
#     
### 5. 활용 키워드 :
![image](https://user-images.githubusercontent.com/76590396/127207796-ca8201c5-ed94-46cc-a310-5ef56d44211d.png)
#  
### 6. 모델링 프로세스
![image](https://user-images.githubusercontent.com/76590396/127205894-3caa2d24-7efa-4f1a-a343-db822b5332fa.png)


#### 1. 아이템 기반 협업 필터링 : 제품 간의 평점을 바탕으로 코사인 유사도로 구현
#### 2. 아이템 기반 협업 필터링의 콜드 스타트 문제가 발생함. 유저들의 구매 데이터가 충분치 않기 때문.
#### 3. 신규 고객 혹은 구매 데이터가 적은 고객들에게 제품 추천을 해주기 위해, 리뷰 텍스트를 바탕으로 카테고리 예측 모델 구현
#### 4. 고객의 검색어, 문의 내용 등을 활용하여, 해당 고객이 관심이 있는 단어들을 통해 카테고리 예측함. 그리고 유저가 구매하지 않은 제품 중 제품 간의 유사도가 높은 상위 5개 제품을 추천해주는 방식으로 구현
#### 5. 카테고리별, 제품 간의 평균 평점에다가 누적 구매 수량을 100으로 나눈 값을 가중치로 더한 새로운 평점을 만듬.
#### 6. 카테고리별, 새로운 평점 상위 5개의 제품을 추천해줌

![image](https://user-images.githubusercontent.com/76590396/127203202-3157dae2-5ceb-4291-beb4-e369905d253a.png)
#### (위 이미지에 대한 참고 사항) New Rating = 새로운 평점 / Mean Ratning = 제품의 평균 평점 / Total Amount = 제품의 누적 판매 수량
### 7. 결과
#### 7-1.앙상블 모델 성능
![image](https://user-images.githubusercontent.com/76590396/127200424-3ee73e96-cbba-43dd-9a3a-3b87bd2e11f7.png)
#### -RFC(랜덤포레스트), RFC_CV(랜덤포레스트, GridSearchCV), XGB(XGBoost), XGB_CV(XGBoost, GridSearchCV)
#### -앙상블의 공통적으로 들어간 요소 : Chi2, TF-IDF

#### 7-2.딥러닝 모델 성능
![image](https://user-images.githubusercontent.com/76590396/127201121-828f6530-4bad-4c39-9f47-015dc7e604a3.png)
#### -LSTM, LSTM with Attention, LSTM(Glove), BERT, LSTM(Glove) with attention, Seq2Seq(LSTM with attention)
#### 결과 : 앙상블 모델과 딥러닝 모델 중, 가장 높은 성능을 보인 모델은 Sequence to Sequence 형태의 LSTM with Attention 모델로, 성능이 0.91이 나왔음.
![image](https://user-images.githubusercontent.com/76590396/127201253-a5b87f31-6a3d-4fbf-a240-036443d45be6.png)
![image](https://user-images.githubusercontent.com/76590396/127201284-6d20849d-799e-427f-aee2-289a5bca1d1d.png)
#### epochs = 50, patience = 15로 학습을 진행하며 Early Stopping을 활용하였음.
#### 그래서, 시각화 자료에서 도중에 끊긴 그래프들이 보임. 이는 Early Stopping으로 빠르게 손실이 최소화되는 구간을 찾았기 때문임.
#### 7-3. 새로운 평점으로 상위 5개 제품 추천
![image](https://user-images.githubusercontent.com/76590396/127204318-b4b88265-6ff0-4223-aa59-77baf0f2ea7b.png)
#### 왼쪽 이미지는, 단순하게 평균 평점만으로 상위 5개 제품을 추천해준 것인데, 이러한 방식은 1명이 구매하고, 평점이 5점인 경우로만 나타나게 됨. 그러므로, 해당 평점에 대한 신뢰도가 다소 부족하다고 판단하였음.
#### 그래서 누적 구매 수량을 가중치로 더하여, 오른쪽 이미지처럼 단순 평균 평점과 완전히 다른 신뢰도가 있는 상품을 추천해줄 수 있게 됨.
#
### 8. 결론
#### - 
