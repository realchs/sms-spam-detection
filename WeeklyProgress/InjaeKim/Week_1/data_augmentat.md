# Data augmentation

### Method 1: Rule-based augmentation

- **EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks**
    - 4가지 간단하지만 파워풀한 operations으로 데이터 증강을 함.
    
    <img src="https://user-images.githubusercontent.com/78612464/209906479-6a84293c-3bdd-460e-afa8-5d1c98ebae70.png"  width="300">
    
    - 4가지 operations
        1. SR: 특정 단어를 유의어로 교체
        2. RI: 임의의 단어를 삽입(insertion)하는 방식
        3. **RD: 임의의 단어를 삭제(Deletion)하는 방식**
        4. **RS: 임의의 단어를 서로 교체(Swap)하는 방식**
        
        → SR과 RI는 한국어로 적용할 때 의미가 변형되는 경우가 많아 **RD와 RS를 위주로 사용하는 게 좋을 것으로 보임.**
        
    - Open source
        - github: [https://github.com/jasonwei20/eda_nlp](https://github.com/jasonwei20/eda_nlp)
        - 한국어 버젼: [https://github.com/catSirup/KorEDA/tree/master](https://github.com/catSirup/KorEDA/tree/master)
        - https://github.com/jucho2725/ktextaug

### Method 2: Learning-based augmentation

- **[GENIUS: Sketch-based Language Model Pre-training via Extreme and Selective Masking for Text Generation and Augmentation](https://arxiv.org/abs/2211.10330)**
    

    <img src="https://user-images.githubusercontent.com/78612464/209906484-7ad0dfb8-10b8-45a0-a9ed-b73a6ba5c194.png"  width="800">

    
    - https://github.com/beyondguo/genius
    - **data augmentation tool** for **various NLP tasks**
    - 한국어 없음. (영어 중국어)
- ChatGPT
    - [https://openai.com/blog/chatgpt/](https://openai.com/blog/chatgpt/)
    - 한국어도 지원하는 ChatGPT를 이용해서 다양하게 데이터 변경 가능.
    - 무료 API 사용 가능 할 듯.?

<img src="https://user-images.githubusercontent.com/78612464/209906706-73e8d9e6-d686-4864-be49-d8bff916341b.png"  width="500">

### Method 3: Learning-based data generation

- Large language model(gpt, bert, t5 …)을 사용하여 finetuning을 하는게 좋을 듯 하다.
- 한글 large language model에는 kogpt([hugging face](https://huggingface.co/kakaobrain/kogpt))
- condition
    - **TF-IDF:** 단어마다 점수를 매겨서 중요도를 표시
    - RAKE: Rapid Automatic Keyword Extraction Algorithm
        - 참고: [https://pongdangstory.tistory.com/368](https://pongdangstory.tistory.com/368)
    - **keyword extraction with BERT**: [https://towardsdatascience.com/keyword-extraction-with-bert-724efca412ea](https://towardsdatascience.com/keyword-extraction-with-bert-724efca412ea)
- 참고: [https://towardsdatascience.com/conditional-text-generation-by-fine-tuning-gpt-2-11c1a9fc639d](https://towardsdatascience.com/conditional-text-generation-by-fine-tuning-gpt-2-11c1a9fc639d)
