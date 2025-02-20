# 단체 퀴즈용 Quiz LLM 제작

## 개요
- 단체 퀴즈방 : 서비스의 접속한 사용자들이 채팅방에 접속하여 퀴즈에 참여
- 퀴즈 생성 : 5분마다 새로운 퀴즈 생성
  - 문제 중복을 피하기 위해 1시간 마다 12개의 주제를 생성
  - 생성된 주제들은 캐시에 넣어놓고 문제가 생성될 때만 호출하여 사용
  - 주제마다 사용 여부를 표시하여 이미 출제된 주제는 제외

## 의존성
- `pydantic` : 구조화된 출력 
  - 안정적으로 같은 구조의 `Json` 응답을 받기 위한 설정
- `django.core.cache` : 캐시를 사용하여 퀴즈 주제를 확인

```py
import os
import json
import openai
from openai import OpenAI
from pydantic import BaseModel
from operator import itemgetter
from django.core.cache import cache
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai.api_key)
```

## 캐시 설정
- 캐시에 저장된 주제가 있는지 확인
- 저장된 주제가 있는 경우
  - 사용되지 않은 `done = False` 인 주제를 꺼내서 전달
  - 선택된 주제를 `done = True`로 변경하여 캐시 갱신

```py
def chat_quiz():
    cache_key = "chat_quiz"
    subjects = cache.get(cache_key)
    selected_subject = ""

    if subjects:
        print(f"\n<--------------캐시 호출-------------->\n")
        subject_list = subjects["subjects"]
        for subject in subject_list:
            if subject["done"] == False:
                subject["done"] = True
                selected_subject = subject
                print(
                    f"<--------------선택된 주제--------------> \n {selected_subject}\n"
                )
                break
            
        if selected_subject:
            print(f"\n<--------------주제 선택/캐시 적용-------------->\n")
            cache.set(cache_key, subjects, timeout=60 * 60)
```

## 새로운 주제 생성
- 주제가 모두 사용되어 `done = False`인 주제가 없는 경우
- 최초 퀴즈 생성인 경우

```py
        else:
            subjects = None
            print(f"\n<--------------주제 모두 사용-------------->\n")

    if not subjects:
        print(f"\n<--------------캐시 없음/주제 모두 사용-------------->\n")
```

### 주제 생성 LLM
- `Subjects` , `Subject` : 주제 데이터의 형태 설정

```py
        # 주제, 난이도 생성 / 한시간에 12개 - 5분에 하나
        class Subject(BaseModel):
            subject: str
            difficulty: str
            done: bool  # 이미 사용된 주제는 false 처리

        class Subjects(BaseModel):
            subjects: list[Subject]

        prompt = f"""
        프로그래밍에 관련된 주제 12개를 생성해줘
        어려움
        done 은 모두 false
        """

        completion = client.beta.chat.completions.parse(
            model="gpt-4o",  # 조정 필요
            messages=[
                {"role": "system", "content": prompt},
            ],
            temperature=0.7,  # 조정 필요
            response_format=Subjects,
        )
```

### 주제 생성
- 새로운 주제를 생성
- 주제를 선택하여 전달
- 선택된 주제 상태를 `done=True` 로 변경하여 캐시 갱신

```py
        subject = completion.choices[0].message.parsed
        subject_json = json.dumps(subject.model_dump(), indent=2)
        subject_dict = json.loads(subject_json)
        print(f"<--------------생성된 주제--------------> \n {subject_dict}\n")
        subject_list = subject_dict["subjects"]
        print(f"<--------------주제 리스트--------------> \n {subject_list}\n")
        for subject in subject_list:
            if subject["done"] == False:
                subject["done"] = True
                selected_subject = subject
                print(
                    f"<--------------선택된 주제--------------> \n {selected_subject}\n"
                )
                break
        cache.set(cache_key, subject_dict, timeout=60 * 60)
```

## 퀴즈 생성 LLM
- `ChatQuiz` : 문제, 선택지, 정답으로 구성

```py
    class ChatQuiz(BaseModel):
        description: str
        choices: str
        answer: int

    prompt = f"""
        {selected_subject}
        주제를 참고하여 프로그래밍에 관련된 문제를 생성해줘
        done : true 로 되어있는 주제는 제외하고 생성

        description 은 문제 내용/설명
        choices 선택지
        answer 정답은 번호
        """

    completion = client.beta.chat.completions.parse(
        model="gpt-4o",  # 조정 필요
        messages=[
            {"role": "system", "content": prompt},
        ],
        temperature=0.5,  # 조정 필요
        response_format=ChatQuiz,
    )
```

### 응답 변환
- `Json` 파일로 전달된 응답결과를 **Python** 딕셔너리로 변환
- **Websocket** 채팅방에서 사용하기 적합한 형태로 변환하여 전달

```py
    quiz = completion.choices[0].message.parsed
    quiz_json = json.dumps(quiz.model_dump(), indent=2)
    quiz_dict = json.loads(quiz_json)
    question = f"{quiz_dict['description']} \n\n {quiz_dict['choices']}"
    answer = str(quiz_dict['answer'])
    return question, answer
```

### Websocket - `consumers.py`
- 퀴즈를 생성하여 클래스 변수로 설정

```py
class ChatConsumer(AsyncWebsocketConsumer):
    pop_quiz_active = False  # POP QUIZ 활성화 상태
    correct_answer_user = None  # 정답을 맞춘 유저
    question = ""
    quiz_answer = ""
    question, quiz_answer = chat_quiz()
    print(f"처음 생성된 퀴즈: {question}, 정답: {quiz_answer}")

    ...
```