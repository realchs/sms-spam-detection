## ELECTRA

- **Masked Language Modeling**(MLM)
    - input 문장의 일부 토큰을 [MASK] 토큰으로 교체하고 mask 토큰을 예측하는 학습 방법
    - [MASK] 토큰이 있는 부분만 직접적으로 학습에 관여하므로, 수 많은 corpus가 필요하다.
    
     <img src="https://user-images.githubusercontent.com/78612464/213632498-8d5a5e07-19a7-4ab9-8869-bb4a5fe7ea59.png"  width="600">
 
    
- **Replaced Token Detection - ELECTRA**
    - 일부 토큰을 [MASK] 토큰으로 교체하는 것이 아니라 작은 generator 네트워크를 이용해 다른 토큰으로 교체하고, 각각의 토큰이 교체되었는지 맞추는 학습 방법
    - 각각의 토큰이 변경되었는지 아닌지 판단하므로 MLM 보다 더 효율적으로 데이터를 사용한다는 해석.
    
    <img src="https://user-images.githubusercontent.com/78612464/213632506-3edbe6b3-5491-4483-a5d7-1cfccaba0903.png"  width="600">
    


    

---

## KoELECTRA

- 45G 말뭉치 (신문, 문어, 구어, 메신저, 웹)

<img src="https://user-images.githubusercontent.com/78612464/213632511-b1a0b086-27ae-44a1-a510-8f037f515eb6.png"  width="600">

### Hugging Face

- [https://huggingface.co/monologg/koelectra-base-v3-discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator)
    
    <img src="https://user-images.githubusercontent.com/78612464/213632516-13f1c1b8-bf72-4f52-91b9-dbf122d6672e.png"  width="900">

    

## 비교-KoBERT

[https://github.com/Beomi/KcBERT](https://github.com/Beomi/KcBERT)

---

# 키워드 & 토픽 추출

1. **대부분의 모델들은 영어 기반 or 문서 수준의 데이터 기반 (ex KeyBERT, BERTopic)**
    1. 짧은 문자 메시지에서 일관되게 뽑을 수 있을 지…
2. **각각의 문자의 키워드가 아닌, 데이터 전체적으로 어떤 문자가 많이 오는지를 알고 싶으면 전체 데이터를 하나의 문서로 생각하고 처리할 수 있을 것 같음**
    1. 중복되는 데이터들에 대해 전처리가 필요할 것으로 보임
        1. Lexical Similarity
        2. Structural Similarity
        3. Semantic Similarity
3. 각각의 문자 키워드는 chatgpt를 활용하는 게 가장 좋을 듯 함.
    
    <img src="https://user-images.githubusercontent.com/78612464/213632521-f12e7f5f-9705-4c3b-ba13-b1134fb2c45e.png"  width="600">

    

---

## Chatgpt API

[https://github.com/transitive-bullshit/chatgpt-api](https://github.com/transitive-bullshit/chatgpt-api)

1. Install

```bash
git clone [https://github.com/transitive-bullshit/chatgpt-api.git](https://github.com/transitive-bullshit/chatgpt-api.git)
cd chatgpt-api
npm install chatgpt puppeteer
```

1. 로그인 정보 입력
    - .env.example 파일에 아이디 비밀번호 입력하고 .env 로 파일명 변경

<img src="https://user-images.githubusercontent.com/78612464/213632523-0b223b51-7785-4634-8b84-ce51d1e04361.png"  width="600">

1. Demo 확인

```bash
npx tsx demos/demo-conversation.ts
```
