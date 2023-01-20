## 스팸 데이터 분석 & 전처리

- 일별 스팸으로 분류된 메세지
- 기간 : 2022.08.14 ~ 2022.12.31
- 컬럼 : seq, 신고유형, 스팸유형, 회신번호, 원발신번호, 중계사, 수신시간, 신고시간, 메시지, 메시지 타입, 저장시간, 파일이름
- 전처리 후 데이터 개수 : 9107416개
    - 음성(신고)에 해당하는 행 제외
    - 스팸유형이 NaN인 행 제외
    - 컬럼으로 스팸유형, 메시지만 남김
- 스팸 유형 Count
<img src=./spam_week3_img1.png width=600>

- 메시지 타입 Count

<img src=./spam_week3_img2.png width=600>

## Text Analysis
### Text Clustering

- **Korean-BERT**
- **t-SNE**
