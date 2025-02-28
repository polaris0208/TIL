# AI 활용 개념과 Hugging Face
> [¶ AI 활용 개념](#ai-활용-개념)<br>
> [¶ Hugging Face](#hugging-face)

# AI 활용 개념

## 연구 vs 활용
### 연구: AI의 성능 향상이 목적
- 모델 개선 또는 개발
- 수학적으로 구조적으로 복잡한 내용

### 활용 : 이미 만들어진 모델 & 서비스 이용
- 모델을 개발할 필요없이 바로 이용
- 다양한 모델을 결합하여 사용 가능
- 의미있게 활용하기 위한 이해가 필수적

## API 개념
>**Application Programming Interface** 
- 프로그램 끼리 통신하는 방식
- AI 서비스가 제공하는 프로그램과 자신의 프로그램을 연결하는 개념
- **ChatGPT, ElevenLabs** 등

## 사전학습 모델
> **Pre Trained Model**
- 많은 학습 데이터로 사전 학습된 모델
- 다양한 모델과 결합 가능
- 검증이 끝난 모델로 안정성이 높음
- 직접 개발 할 경우 많은 데이터가 필요: 모델이 무겁고 불안정

## AI 활용의 주의점
- 기존 모델을 활용할 경우 중요한 것은 **Fine Tuning**
- AI에 대한 이해가 부족할 경우 문제점 발생
  - 성능을 이끌어 내지 못하는 경우
  - 사용 중 발생하는 문제에 대처 불가능
  - 수많은 모델 중에서 적합한 모델 선별의 문제
  - 결과를 해석하지 못하는 문제

[¶ Top](#ai-활용-개념과-hugging-face)

# Hugging Face 
> AI 모델 제공 및 다양한 기능 제공 [¶](https://huggingface.co) <br>
> 커뮤니티가 크게 발달

- 최신 모델. 검증된 모델 제공하는 허브역할
- 개발, 학습 과정 생략 가능
- 오픈 소스 커뮤니티에서 수많은 개발자가 함께 개발한 모델 사용 가능
- 다양한 개발자와 의견 교환 가능

## 장점
- 쉬운 접근성 : 쉽고 직관적, 이해하기 쉬운 예시
- 광범위한 모델선택 : 다양한 언어
- 강력한 커뮤니티 : 적극적인 소통 가능 

## 단점
- 리소스 요구량
- 복잡한 초기 설정
- 특화된 모델 : **NLP**

## 실습

### 패키지 설치

#### Tip
- 주피터 노트북에서 ! 입력 후 코드 작성하면 시스템 명령어 사용 가능
- 터미널에서 파이썬 사용 시 python이 아닌 python3 입력

#### 가상환경 활성화

```bash
python3 -m venv AI # 생성
source AI/bin/activate
```
#### 필요 패키지 설치

```py
pip install --upgrade pip
pip install ipykernel
pip install transformers
pip install torch torchvision
```

#### ipykernel 설정

```bash
python -m ipykernel install --user --name AI --display-name AI
```

#### 경고 문구 설정
- 활성화 `action='default'`
- 비활성화 `action='ignore'`

```py
import warnings
warnings.filterwarnings(action ='ignore')
```

#### 모델 불러오기, 설정

```py
from transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
```

#### 모델 적용

```py
# 데이터 입력
text = "My name is"
encoded_input = tokenizer(text, return_tensors='pt') # 모델이 학습하기 위한 텐서 데이터로 변환
encoded_input
#
{'input_ids': tensor([[3666, 1438,  318]]), 'attention_mask': tensor([[1, 1, 1]])}

# 결과 출력
output = model.generate(encoded_input['input_ids'], max_length = 50)
generated_text = tokenizer.decode(output[0], skip_special_tokens= True) # 사람이 이해하기 위한 형태로 변환
generated_text
#
"My name is John. I'm a man of God. I'm a man of God. I'm a man of God. I'm a man of God. I'm a man of God. I'm a man of God. I'm a"
```

### 결론
> 간단학게 모델을 구현하고 활용가능<br>
> 사용법과 발생 가능한 문제점을 미리 파악하여야 함

[¶ Top](#ai-활용-개념과-hugging-face)


