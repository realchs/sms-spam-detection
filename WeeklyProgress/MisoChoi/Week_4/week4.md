## 개인 데이터 키워드/토픽 분석

데이터
- 1268개
- 개인 메세지(SMS+MMS) 백업 데이터
- 저장된 번호와 주고받은 메세지 제외
- 키워드 필터링 & Regex

후보 모델
- Korean Contextualized Topic Models
- **KoBERTopic**


## KoBERTopic ([github](https://github.com/ukairia777/KoBERTopic))
- KoBERTopic은 BERTopic을 한국어 데이터에 적용할 수 있도록 토크나이저와 BERT를 수정한 모델.
  - BERTopic is a topic modeling technique that leverages transformers and c-TF-IDF to create dense clusters allowing for easily interpretable topics whilst keeping important words in the topic descriptions.
- 토크나이저로는 형태소 분석기 Mecab을 사용.
- BERT로는 다국어 SBERT인 'sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens'를 사용.
- 토픽의 수는 임의로 50으로 결정.
- 별도 불용어 제거 등의 추가 전처리는 진행 X. (진행할 경우 더 좋은 결과를 얻을 수 있을 것으로 기대.)

시각화(BERTopic github에 있는 예시)
![image](https://user-images.githubusercontent.com/78155086/213619803-4216d530-687f-4298-8fe3-90fd736f911f.png)
![image](https://user-images.githubusercontent.com/78155086/213619814-356d9edd-10ff-4896-a03c-51f270d69e85.png)






