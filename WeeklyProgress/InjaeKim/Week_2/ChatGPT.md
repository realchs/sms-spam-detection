# ChatGPT 활용 방안

1. task별로 fine-tuning을 위한 수만~수십만개의 데이터를 모으는 것은 비현실적임
2. 또한 현재 인턴쉽 프로젝트에서는 추가적인 model fine tuning할 resource도 부족함.
3. pre-training에서 학습한 분포와 task에서 학습한 분포와의 차이로 인해 generalization 능력이 약화되며, task 성능이 좋더라도 해당 task에만 해당되는 over-fitting된 결과일 수 있다.

## 1. Prompt Engineering ( In-context Learning )

 <img src="https://user-images.githubusercontent.com/78612464/210357414-74d8e341-aa1e-4202-b737-367a2ef0a8ab.png"  width="400">



- 학습 없이 가능
- 프롬프트 입력 방법을 잘 찾아 내야함.
    - 참고: https://github.com/f/awesome-chatgpt-prompts

<img src="https://user-images.githubusercontent.com/78612464/210357501-d9a3793b-2a68-4f0a-97ae-a98a5f2d0aa2.png"  width="600">

- GPT3는 example이 몇개만 주어진다면 prompt에 대한 출력이 매우 안정적이며 반복적으로 알맞은 결과가 나온다.
    
    <img src="https://user-images.githubusercontent.com/78612464/210357592-73d328fe-31ec-4a69-8363-a7ffbf87ee8f.png"  width="600">
    

## 2. Prompt based tuning (P-tuning)

<img src="https://user-images.githubusercontent.com/78612464/210357594-abd388c8-c239-4c82-a30b-d6bcb9506dd1.png"  width="600">

- paper
    - [**GPT Understands, Too](https://arxiv.org/pdf/2103.10385.pdf)**
    - (Liu, Xiao, et al. "GPT understands, too." *arXiv preprint arXiv:2103.10385* (2021).)
- Pre-trained model은 freeze하고, prompt encoder(적은 parameter)만 학습에 사용하는 방법

## 3. **LoRA : Low-Rank Adaptation**

<img src="https://user-images.githubusercontent.com/78612464/210357598-f983aefb-99f6-478b-946f-a80de801d9e2.png"  width="400">

- paper
    - [**Lora: Low-rank adaptation of large language models**](https://arxiv.org/abs/2106.09685)
    - Hu, Edward J., et al. "Lora: Low-rank adaptation of large language models." *arXiv preprint arXiv:2106.09685*
     (2021).
- 주황색 부분만 추가하여 학습한다.
