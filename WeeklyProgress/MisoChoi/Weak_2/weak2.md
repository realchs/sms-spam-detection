### 지난주 계획

- 저장된 번호 포함
- Presidio Analyzer 사용하여 익명화
- spaCy

### 진행 결과

- 아이폰 유저는 iCloud 통해 문자 백업
- SMS 외에도 MMS 데이터 추가함. (MMS는 스팸과 구분하기 더 어려운 햄 데이터)
- 저장된 번호 포함
    ⇒ 개인정보 문제… 저장된 번호 제외?
 
- Presidio Analyzer 사용하여 익명화
    - 한국어 데이터에서 Presidio Analyzer 사용이 어려움
    - (1) 우선 presidio analyzer가 영어만 지원함
    - (2) SpaCy korean 모델은 다운받아서 사용 가능함(Tokenization, NER 등 기능 지원). 그러나 presidio analyzer와 같이 사용이 어려움
- Deny-list based PII recognition
- Regex based PII recognition
  - 숫자를 Regex(Regular Expression) 기반으로 찾고 같은 개수의 랜덤 숫자로 대체
- Calling an external service for PII detection
  - 개체명  (PER(person), LOC(location)) 등을 찾고 다른 여러 샘플들 중 하나로 대체
    - KoBERT + CRF로 만든 한국어 개체명(NER) 인식기 github[[링크](https://github.com/eagle705/pytorch-bert-crf-ner)] 이용하려 하였으나 weight를 받을 수 없음..…
    - spaCy korean 모델[[링크](https://spacy.io/models/ko)]사용해서 고유명사(PROPN)를 다른 대체 리스트 중 랜덤 원소로 대체
