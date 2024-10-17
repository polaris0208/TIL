## Attention
> 시퀀스 데이터에서 중요한 부분에 더 많은 가중치 할당
> 정보를 더 효율적으로 처리하는 기법

### 개념
1. 기본 구성 요소와 동작 방식
#### Attention 메커니즘
- 자연어 처리(NLP), 시계열 데이터, 기계 번역, 오약, 질의 응답
#### 동작 방식
1. 구성
- 답(key)-질문(query)-최종요약(value) 
- 입력의 sequence를 분석
- 중요도를 파악
- 가중치 부여(일관되게 부여)
2. Attention 스코어(중요도)
- query 와 key 간의 유사도를 측정
- 백터의 내적(dot product) 사용
- softmax = attention스코어를 확률 분포로 변환 = 가중치의 합을  1로
- attention = 가중치 x value
3. sel - Multi-head attention
- self : 시퀀스 내의 각 요소
- multi-head : 여러개의 self attentiondmf 병렬로 수행
  - 모델이 다양한 관점에서 데이터를 처리

### 예시 
> the cat sat on the mat because it was tired

```teacher, "what is 'it'```
```most of students, "cat"```
```the others, "mat"```
- 선생님이 질문한 "it" 은 query
- 대부분의 학생이 대답한 "cat" 은 key 
- 일부 학생이 대답한 "mat"는 value
1. it, cat, mat의 유사도를 확인
2. 가중치를 계산
3. 각 단어의 관계를 확인하여 문장을 더 잘 이해하게 됨

-----------

## NLP
> 자연어 처리 모델
### 워드 임베딩(Word Embedding)
- 단어를 고정된 크기의 백터(숫자)로 변환
- 유사한 단어들은 유사한 숫자로 변환
- Word2Vec, GloVe
1. Word2Vec
- CBOW: 주변 단어(context)를 보고 중심 단어(target)를 예측
- Skip-gram: context를 보고 target 예측
2. GloVe(Global vectors for Word Representation)
- 단어-단어 공기 행렬(word-word co-occurrence matrix)
- 전역적인 통계 정보를 통해 단어 간의 의미적 유사성을 반영

### 시퀀스 모델링(Sequence Modeling)
- 순차적인 데이터 처리
- RNN, LSTM, GRU

### Trnasformer & BERT
1. transformer
- 순차적인 데이터 병렬 처리
- 자연어 처리에 뛰어난 성능
- Encoder-Decoder 구조
  - Encoder: 입력 시퀀스 처리, 인코딩된 표현 생성
    - self-attention: 문장 내 관계 학습 
    - Feed-Foward Neural Network -> 새로운 백터로 변환
  - Decoder
    - 시작 토큰 입력
    - taget 단어를 고정된 백터로 변환
    - positional encoding 수행
    - masked multi-head attenrion self attention
      - 이전의 단어들로만 예측하도록 마스킹하여 self attention 수헹
    - 인코더-디코더 attention: 디코더가 인코더 연결- 입력 문자 참조
    - FFNN를 통해 추가로 백터 변환
  - 위 과정을 반복하여 오차를 줄여나감
  - 종료 토큰이 예측되면 번역 종료

2. BERT
(Bidirectional Encoder Representations from Transformers)
- Transformer인코더 기반 사전 학습된 모델
- 양방향으로 문맥을 이해
- 다양한 자연어 처리 가능
- 사전학습(Pre-Training)
  - 대규모 텍스트 코퍼스
  - Masked Language Mode과 Next Sentence Prediction 작업
- Fine-tuning
  - 사전 학습된 BERT를 파인 튜닝하여 사용
  - 텍스트의 분류, 질의 응답, 텍스트 생성 등 다양한 자연어 처리 작업