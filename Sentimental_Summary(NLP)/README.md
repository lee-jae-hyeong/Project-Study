개인프로젝트
### 1. 주제 : Amazon Food Reviews 감성 분석 및 요약문 추출
### 2. 주제 선정 이유 
##### - 이전에 커머스 MD로 근무하면서, VOC나 고객 리뷰 등을 대략적으로 볼 수 있지만, 이를 자동적으로 분류하여 어떠한 부분이 이슈가 있는지 파악하는데 생각보다 많은 시간이 할애 되었음. 
##### - 그래서 이를 개선하여, 리뷰나 VOC의 요약문을 추출하고, 그 요약문이 해당하는 이슈사항을 카테고리별로 자동으로 분류할 수 있는 것을 구현해볼 수 있다면 좋겠다라는 생각으로 시작하였음. 
##### - 이러한 시스템이 구현하게 된다면, 기업 측에서는 불필요한 인력 낭비를 줄일 수 있고, 고객님들이 어떠한 부분에서 불편함을 겪고 있는지 직관적으로 파악할 수 있어 이를 개선하는 활동을 우선순위에 따라 정할 수 있음.
### 3. 데이터 : Amazon Food Reviews Data로 1999년 10월 - 2012년 10월의 리뷰 기재
##### - Feature data : 568,454 x 10
##### - URL : https://www.kaggle.com/snap/amazon-fine-food-reviews
### 4. 활용 키워드 : EDA, Data Visualization, DL(LSTM, Attention), ML(RandomForest, XGboost), Tensorflow  등
### 5. 모델링 프로세스
##### 평점이 5점인 리뷰의 경우 1로 치환, 평점이 4점 이하인 리뷰의 경우 0으로 치환하여 감성 분석 모델 구현 - ML과 DL 성능 비교 실시
##### 리뷰 텍스트를 Feature로 설정, 요약문을 label로 설정하여 LSTM with Attention 모델 구현
### 5. 가설 설정 : 5점인 경우, 부정적인 내용이 없으므로 긍정, 4점 이하의 경우, 부정적인 내용이 있을 가능성이 높으므로 부정으로 분류가 가능하다.

### 6. 모델 성능
#### - 감성 분석 모델(Accuracy 기준)
##### 1. Version1 : LSTM Model(0.88)
##### 2. Version2 : RadomForest(0.63), XGBoost(0.62), LSTM(0.63), BERT(0.81)

#### - 요약문 모델(Accuracy 기준)
##### 1. Version1 : LSTM with Attention(0.70)
##### 2. Version2 : LSTM with Attention(0.64)
### 7. 배운점


#### 5. 결론
##### - 
