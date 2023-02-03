# Model Agnostic vs Model specific

## Model Agnositic

### 1. LIME (2016)

<img src="https://user-images.githubusercontent.com/78612464/216529695-d495ae5d-8994-4f31-8234-fe2e59f977cf.png"  width="700">

- Local Surrogate model
    - surrogate model: 분석이 힘들 모델을 분석이 쉬운 모델을 대체제로 이용해 분석하는 방법
    - 학습데이터 전체를 이용하는 것이 아닌 한개 씩 이용하므로 **local surrogate analysis**
    - $\xi(x) = \underset{g \in G}{\operatorname{\arg min}} L(f, g, \pi_x ) + \Omega(g)$
        - $L(f, g, \pi_x )=\sum_{z,z^\prime\in{Z}}\pi_x(z)(f(z)-g(z^\prime))^2$
            
            <img src="https://user-images.githubusercontent.com/78612464/216529703-33e9e85a-68d8-412e-8009-1373fa9a0129.png"  width="300">
            
        - 
            - $f$: 해석하려는 모델
            - $z$: input data x를 perturb한 데이터
            - $g$: surrogate model
            - $z^\prime$: 차원 축소된 $z$
            - $\pi_x$: z의 가중치 - x와 z 사이의 거리로 결정
        - $\Omega(g)$: 모델 복잡도
            - 해석할 수 있는 단순한 모델
        - 예를 들어 local surrogate model $g(z)$를 회귀 모델로 정의 했으면
            - $g(z) = w_0z_0+w_1z_1+ ... + w_nz_n$
            - 학습이 끝난 가중치 $w$의 값을 통해 중요도를 예측할 수 있다.
- 파생 연구
    1. ~~SLIME(Sound-LIME)~~
        1. ~~음성 데이터~~
    2. KL-LIME
    3. DLIME
    4. QLIME(Quadratic-Lime)

### 2. SHAP (2017)

- Shapley Values
    
    <img src="https://user-images.githubusercontent.com/78612464/216529706-63d29dba-d7a5-4d18-b656-c3e2bbd33a0a.png"  width="600">
    
    - 특정 플레이어 존재 여부에 따른 상금 변화량 **Marginal contributions를 계산 후 평균을 구함.**
- 모델의 input → 플레이어
모델의 예측 → 상금
- 파생 연구
    1. KernelSHAP
    2. LinearSHAP
    3. DeepSHAP

### 3. Anchor

### 4. L2X

## Model specific

### ****Transformer Interpretability Beyond Attention Visualization (CVPR2021)****

<img src="https://user-images.githubusercontent.com/78612464/216529710-76889160-0143-49c3-946e-a8e2c1076127.png"  width="400">

- 기존 방식
    - attention == relevancy score
    - multiple layer를 결합 (ex. attention 평균)
    - attention rollout
