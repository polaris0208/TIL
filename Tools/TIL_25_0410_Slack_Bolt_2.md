# Slack 봇 + LangChain + OpenAI 연동 정리

## 핵심 구성 요소

- `slack_bolt`: Slack 앱 개발을 위한 파이썬 SDK. 이벤트 기반 처리 가능.
- `SocketModeHandler`: Slack 서버와 실시간 통신을 위한 소켓 핸들러.
- `langchain`: 프롬프트 템플릿, 체인, 메모리 등을 통해 LLM 활용을 도와주는 라이브러리.
- `langchain_openai.ChatOpenAI`: OpenAI GPT 모델을 LangChain 체인에서 사용 가능하게 해주는 클래스.
- `ConversationBufferWindowMemory`: 대화 내용을 최근 `k`개까지 기억하여 문맥 유지.
- `.env`: 환경변수 관리를 위한 파일. Slack Token과 같은 비밀 정보 저장.

---

## 동작 개요

- Slack에서 사용자가 메시지를 입력하면 해당 메시지를 LLM으로 전달.
- LangChain의 `LLMChain`이 템플릿과 함께 메시지를 처리하고 응답 생성.
- 응답을 다시 Slack에 전송하여 사용자에게 표시.

---

## 코드 흐름 설명

### 환경변수 로딩
```python
import dotenv
dotenv.load_dotenv()
```

---

### Slack 앱 초기화
```python
from slack_bolt import App
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
```

---

### LangChain 구성
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0)
```

---

### 프롬프트 템플릿 정의
```python
from langchain.prompts import PromptTemplate

template = """어시스턴트는 단순한 질문에 답하는 것부터 광범위한 주제에 대해 심도 있는 설명과 토론을 제공하는 등 다양한 작업을 돕도록 설계되었습니다.
...
{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)
```

---

### 체인 정의 및 메모리 설정
```python
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

chatgpt_chain = LLMChain(
    llm=llm, 
    prompt=prompt, 
    memory=ConversationBufferWindowMemory(k=2),
    verbose=True
)
```

---

### Slack 이벤트 처리
```python
@app.event("app_mention")
def handle_app_mention_events(body, say, logger):
    message = body["event"]['text']
    output = chatgpt_chain.predict(human_input=message)  
    say(output)
```

```python
@app.message(".*")
def message_handler(message, say, logger):
    output = chatgpt_chain.predict(human_input=message['text'])   
    say(output)
```

---

### 앱 실행
```python
if __name__ == "__main__":
    from slack_bolt.adapter.socket_mode import SocketModeHandler
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
```

---

## .env 파일 예시

```
SLACK_BOT_TOKEN=xoxb-xxx...
SLACK_APP_TOKEN=xapp-xxx...
```