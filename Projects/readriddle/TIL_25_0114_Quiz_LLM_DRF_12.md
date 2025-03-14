# 챗봇 LLM 개선
> 제목, 대화 내역 등 **DB**에 반영할 데이터 추출이 용이하도록 챗봇 개선

## 의존성 설치
- `pydantic` : 출력 형식 설정

```py
import os
import json
import openai
from openai import OpenAI
from pydantic import BaseModel
openai.api_key = os.getenv("OPENAI_API_KEY")
# Pydantic 모델 정의
```

## 출력 형식 설정
- `ChatHistory` :  대화내역 형식
  - `Assistant` : 챗봇 응답 내용 저장 형식
  - `User` : 사용자 입력 내용 저장 형식
  - `title` : 누적된 대화 내역을 요약하여 최적의 제목을 생성

```py
class Assistant(BaseModel):
    id: int
    content: str

class User(BaseModel):
    id: int
    content: str

class ChatHistory(BaseModel):
    title: str
    response: str
    user_input: User
    ai_response : Assistant
```

## 답변 생성
- 대화내역을 바탕으로 제목 생성
  - 기존방식 : 별도의 **LLM**을 제작하여 생성
- 대화내역을 기준으로 새로운 질문/응답에 `id` 를 부여하고 저장

```py
# OpenAI 클라이언트 설정
client = OpenAI(api_key=openai.api_key)

prompt = """
    **Reply only in Korean**
    make title refer to chat history
    give id to each reaponse refer to chat history
    You are an official documentation Q&A chatbot.  
    1. Answer questions based on the provided official documentation.  
    2. Cite the source of the information and specify the relevant section of the documentation.  
    3. If a question is not related to the official documentation, inform the user.  
    4. For questions about unknown knowledge, respond with: "Sorry, I don't know."  
    5. Include code in your answers whenever possible.  
    6. Maintain the context of the conversation by referencing the chat history.  
    7. If you believe the current question has been addressed, ask: "Do you have any additional questions?"  
    8. If there are no further questions, proceed to the next step.
    
    <context>
    context
    </context>

    <chat history>
    history
    </chat history>
    """

# 퀴즈 데이터를 구조화하여 응답 받기
completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": question},
    ],
    response_format=ChatHistory,  # 여기에서 QuizResponse 모델을 설정
)

# 응답 데이터
quiz = completion.choices[0].message.parsed

# JSON 형태로 추출
quiz_json = json.dumps(quiz.model_dump(), indent=2)
quiz_json = json.loads(quiz_json)

# 출력된 JSON 데이터
print(quiz_json)
```

# SQLite 명령어
- 레퍼런스 데이터를 **DB**로 옯기고 추출하는 과정에서 사용

## SQLite 데이터베이스 시작
- `mydb.db` 데이터베이스 열기, 파일이 없으면 새로 생성

```bash
sqlite3 mydb.db
```

## SQL 파일 가져오기
- `file.sql`  **SQL** 명령어를 실행

```bash
sqlite3 mydb.db < file.sql
```

## SQL 파일로 내보내기
- 데이터를 **SQL** 파일로 저장

```bash
sqlite3 mydb.db .dump > file.sql
```

## JSON 형태로 출력
- **SQLite 3.33.0** 이상
- **JSON** 형태로 출력

```bash
sqlite3 mydb.db
sqlite> .mode json
sqlite> SELECT * FROM table_name;
```

### JSON 파일로 저장

```bash
sqlite3 mydb.db -json -header "SELECT * FROM table_name;" > output.json
```

## SQLite CLI 명령어

### 테이블 목록 보기
- 모든 테이블 표시

```sql
.tables
```

### 테이블 스키마 확인
- **SQL** 정의 표시
- `table_name` : 특정 테이블 지정

```sql
.schema 
.schema table_name
```

### 데이터 출력 형식 변경
- 기본 형식
- CSV 형식
- JSON 형식 **(SQLite 3.33.0 이상)**

  ```sql
  .mode column
  ```

  ```sql
  .mode csv
  ```

  ```sql
  .mode json
  ```

### 결과를 파일로 저장
- 명령의 출력이 `file_name`에 저장
- `stdout` : 기본 출력으로 되돌리기

```sql
.output file_name
.output stdout
```

## 데이터베이스 종료

```sql
.exit
.quit
```