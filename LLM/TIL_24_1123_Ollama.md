# Ollama
> 오픈 소스 대규모 언어 모델 제공<br>
> 로컬 환경에서 **LLM** 구동 가능

## ollama 프로그램 활용

### ollama 웹사이트 접속 [¶](https://ollama.com/)
- 운영 체제에 맞춰 설치 파일 다운로드 및 실행

### 터미널에서 실행
- `ollama`

### 모델 다운로드
- `ollama pull <모델 이름>` : 모델 다운로드
- `ollama run <모델 이름>` : 모델 실행, 없으면 다운로드

### 모델 종류
- `qwen2.5-coder` : 코드 작성 특화 모델
- `gemma` : 구글 `gemini` 의 경량화 모델, 엔비디아와 협력하여 **GPU** 최적화
- `llama` : 메타에서 개발, 최근 모델의 고성능 버전은 **GPT** 와 비슷한 성능

### 터미널 환경 실행
- `ollama run <모델 이름>` : 입력창에 메시지를 입력하여 대화 시작
- `ctrl + d` : 대화 종료

### 파이썬 환경 실행

#### 메서드
- `list` 목록 호출
- `show` 모델 상세 내용
- `create` `Modelfile`에 맞춰 새로운 모델 구축

#### 기본 대화
- `chat`: 대화의 맥락이 유지, 여러번의 대화에 사용
- `generate` : 1회성 대화, 검색에 사용

```py
import ollama

respones = ollama.chat(model = 'llama3.2:latest', messages=[
  {
    'role' : 'user', 'content' : '하늘이 왜 파란색이야?',
    },
])

print(respones['message']['content'])
```

```
하늘의 màu은 다양한 фактор에 의해 영향을 받습니다. 하늘은 주로.blue색을 띤다, 그러나 실제 하늘의 색상은 그에 따라 달라집니다.

하늘의 blue 색상은 다음 이유로 발생합니다.

1. **광학**: 하늘에서 일으켜지는 광학적 효과가 있습니다.阳光이 Earth surface를 통과할 때, shorter波장(blue wavelength) 보다는 longer wave length(RED wavelength)인iolet 및 red light가 더 강한 영향을 받습니다. 이로 인해 blue light가 Earth surface에 반사되면서 하늘의 blue 색상이 생기고 있습니다.
2. **대気层**: 하늘에서 주로存在하는 대기 layer는 mostly nitrogen gas와 oxygen gas composition으로 구성되어 있습니다. 이러한 가스들은 blue color를 띤다, 따라서 이 color가 하늘에 보이는 방향입니다.
3.  **Earth's atmosphere의 분자 density**: 대기 layer의 분자 density는 지구 중심 부근에서 가장 높은 분자 density로 나타납니다. 이로 인해 blue color가 strongest 것으로 나타납니다.

하늘의 색상은 지구 중 心부와 지구 표면 사이의 경계에 따라 달라집니다. 

- 지구 중부에는 red color이 stronger한색으로, 주로 blue color이 약한 màu을 보입니다.
- 지구 표면에서는 red color이 더 강하게 나타나며, blue color은 약한 색상을 띤다.

이러한 이유로 하늘의 색상은 다양하고, 다양한 조건에 따라 달라집니다.
```

#### langchain 활용
- `langchain` 라이브러리와 연계하여 사용 가능

```py 
import langchain
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1:8b")

querry = ("하늘은 왜 파란색이야")
    
response = llm.invoke(querry)
print(response)
```

```py
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("{topic} 친근한 말투로 초등학생도 이해할 수 있게 쉬운 말로 설명해줘.")

# 체인 생성
chain = prompt | llm | StrOutputParser()

# 간결성을 위해 응답은 터미널에 출력됩니다.
answer = chain.invoke({"topic": "하늘은 왜 파란색이야"})

print(answer)
```

#### 사용 결과
- 답변의 내용은 적절
- 답변 내용에 번역과정에서 처리되지 못한 영어나 한자가 자주 확인됨
- 어투가 정돈되지 못한 모습이 확인됨

```
# 단순 질문

하늘의 색상은 인간이 보는 것과 다를 수도 있습니다. 하늘이 보이는 빛의 특정 부분에 해당하는 파장의 빛인 청색광을 포함하여 여러 가지 빛의 파장이 있다. 이 중에서 주로 사람의 눈으로 보는 청색광과 파란색광의 파장은 450~495ナンボ메터(나노미터)이다.

# 프로프트 적용

하늘이 파란색인 이유를 설명해주면 좋을 것 같아요!

그것은 빛의 주파수가 때문이에요! 빛이 뭐고, 빛의 주파수가 뭔지 모르시나요? 

빛은 우리 눈에 보이는 모든 물체에서 나와, 눈을 통해 들어가는데, 그 빛은 여러 색깔로 나뉠 수 있다고 생각하시면 좋을 것 같아요. 빨강, oranze,黄色,绿색,청녹색,하늘색이 대표적인 예시예요. 

그리고 우리가 보는 색들은 모두 빛의 주파수를 다르게 가지고 있어요. 파란색은 가장 긴 주파수, 빨간색은 가장 짧은 주파수를 가졌거든요!

빛은 모든 물체에서 나와, 그 빛이 공중에 propagate된다면, 모든 물체가 같은 주파수로 빛을 뿜으면서, 하늘이 연한 파란색일 거야!

그러나, 우리 눈에 보는 색깔은 모두 각자 다른 주파수를 가졌기 때문에, 하늘빛만이 파란색으로 보인다! 

이것도 공기와 같은 물질의 재료들이 빛의 파장(주파수)에 영향을 미친다는 것이고, 그 영향때문에 하늘이 보는 색을 파란색으로 유지한다는 거예요!
```


