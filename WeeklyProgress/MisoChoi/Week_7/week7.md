### Convolutional Neural Networks for Sentence Classification (EMNLP, 2014) [[paper](https://arxiv.org/pdf/1408.5882.pdf)]

- Computer Vision 분야에서 사용되어온 CNN 모델을 NLP 태스크에 적용하여 좋은 결과를 냄.
- un-supervision 방식으로 pre-train한 word vectors(word2vec) 위에 convolution layer 1개를 얹어 만든 간단한 CNN 모델.
- 적은 튜닝으로도 좋은 결과 → pre-trained vector가 ‘universal’ feature extractors임을 의미함.
- 추가 튜닝 : fine-tuning으로 task-specific(classification) vector를 학습.

<img src=./conv_sen_fig1.png width=700>

[Backgrounds]

- word embedding : 글자 → 숫자
- CNN (Convolution Neural Networks)
    - CNN 그림
        <img src=./conv.png width=700>
        
    - Convolution : 이미지 특징 추출기
        - *convolution layer와 pooling layer를 여러겹 쌓는 방식으로 구성됨.*
        - convolution
        - pooling : 크기 조정
        
        <img src=./convolution.gif width=250>
        
    - Classifier : 클래스 분류기

### Attention-Based Convolutional Neural Networks for Sentence Classification (INTERSPEECH 2016) [[paper](https://www.isca-speech.org/archive_v0/Interspeech_2016/pdfs/0354.PDF)]

- Motivation
    - 문장 내 연이어 위치해 있지 않은 단어간의 correlation을 학습하기 위해
    - long-term contextual information을 학습하기 위해
- Attention layer를 추가함
    
     <img src=./att_cnn.png width=400>
    
    <img src=./eq3.png width=600>
    <img src=./eq4.png width=600>
    
    - example
        
        There’s not one decent performance from the cast and not one clever line of dialogue.
        
        ⇒ There’s ***not*** one ***decent*** **performance** from the cast and not one clever line of dialogue.
      - 'performance'는 다른 단어들보다 not이나 decent 단어와 갖는 score가 더 클 것임.
