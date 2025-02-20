# Prompt
> 생성형 AI 명령 지시문<br>
>> [¶ Generative AI](#generative-ai)<br>
[¶ LLM](#large-language-model)<br>
[¶ Prompt Engineering](#prompt-engineering)<br>
# Generative AI
> 생성형 **AI**
- 새로운 콘텐츠를 생성 가능한 **AI**

## Rule based Algorhythm & AI Algorhythm
- 공통점: 개발자가 입출력을 설계
- 차이점: 입력과 출력 사이의 알고리즘 구현 주체
  - **Rule based** : 개발자가 구현
  - **AI** : AI가 데이터 학습을 통해 구현

## 생성형 AI 종류
### 이미지
- **DALL-E** [¶](https://openai.com/index/dall-e-3/)
- **Midjourney** [¶](https://www.midjourney.com/home)
- **Stable Diffusion web UI** [¶](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
### 동영상
- **Gen-3** [¶](https://runwayml.com/research/introducing-gen-3-alpha)
- **PixVerse** [¶](https://runwayml.com/research/introducing-gen-3-alpha)
- **Sora** [¶](https://openai.com/index/sora/)
### 텍스트
- **GPT** [¶](https://openai.com/index/gpt-4/)
- **Claude** [¶](https://claude.ai/login?returnTo=%2F%3F)
- **Gemnini** [¶](https://gemini.google.com/?hl=ko)
### 음악
- **Suno** [¶](https://suno.com)
- **Udio** [¶](https://www.udio.com)

# Large Language Model
- 텍스트 생성 및 번역, 질문과 답변. 요약 등의 기능을 하나의 모델이 수행
## 기본 원리
- 입력과 출력 사이
- 조건부 확률 분포를 학습
  - 입력 데이터의 모든 토큰별 확률을 계산
  - 가장 높은 것을 선택 후 출력

## 종류
- **Open AI [¶](https://openai.com): GPT**  : 유료
- **Anthropic [¶](https://docs.anthropic.com/en/home) : Claude** : 유로
  - 개발, 코딩 특화 : 코드 검토, 파라미터 설정 등
- **Perplexity : Perplexity [¶](https://www.perplexity.ai)** : 유료
  - 실시간 대화형
- **Google - Gemini** : 유료
- **Meta - Llama** [¶](https://www.llama.com) : 무료
  - open source : 수정해서 사용 가능

### GPT
- **Generative Pretrained Transformer**
- **Transformer decoder - Autoregressive Model**
  - 이전 시점의 출력을 현재 시점의 입력으로 사용
  - **EOS** 토큰 출력 시까지 반복
  - **EOS : End of Sequence**

### Chat GPT
- **LLM** 모델인 **GPT**를 활용하는 서비스
- 입력 데이터를 바탕으로 **GPT**와 외부도구를 이용해 예측한 데이터를 출력
- 실제 계산을 수행하는 것이 아닌 외부도구를 이용해 연산

#### 한계 및 극복방법
- 데이터 편향: 특정한 관점에서 답변할 가능성
  - 거대한 양의 데이터를 학습시켜 극복중
- 데이터 오류: 잘못된 정보를 학습할 가능성
  - 거대한 양의 데이터를 학습시켜 극복중
- **Hallucination** : 환각 : 실제로는 근거가 없는 그럴듯한 내용의 답변
  - 창의적인 결과를 도출하는 측면도 존재
  - **RAG(Retrieval-Augmented Generation)** [¶](https://aws.amazon.com/ko/what-is/retrieval-augmented-generation/) 기법 활용 
    - 외부 지식 및 데이터 베이스를 참조하도록 지시

#### 올바른 활용법
- 구체적이고 명확한 질문, 배경정보 제공
- 추가 질문과 정보로 대화를 이끌어 나가기
- 대화 주제가 달라진 경우 새로운 대화 생성
- 사실 확인 및 평가
  - 공식 사이트, 참고 문헌 활용
- **Docstrings** : 모듈이나 함수의 목적과 이용에 필요한 세부 정보를 담는 것
- **Deburgginh** : 코드의 오류를 찾고 수정하는 과정

# Prompt Engineering
> 최적의 응답을 생성하도록 입력 프롬프트를 설계 조정
- 최초 프롬프트 입력 후 답변을 확인 후 수정해가면서 작업 수행
> 예문<br>
System: 페르소나 부여 - 특정한 관점에서 답변하도록 유도 ex) 강사의 입장에서
User : 사용자의 명령 
Condition : 조건 
Output Tyep : 출력 형식

[¶ TOP](#prompt)
