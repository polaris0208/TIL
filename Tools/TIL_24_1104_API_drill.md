# API drill
> 실제 **API** 및 모델의 사용방법<br>
>[¶ API Key 등록 및 확인](#api-key-등록-및-확인)<br>
>[¶ API 호출 및 활용](#api-호출-및-활용)

# API Key 등록 및 확인
## 발급
1. **API** 서비스 홈페이지 접속
2. 회원가입
3. **Profile** : 대부분 프로필 내부 **API Key** 메뉴에서 발급 및 관리
  - 발급 이후 코드 재확인 불가
  - 별도의 공간에 저장 필요
4. **API Reference** : **API** 및 **API Key** 사용방법에 대한 문서 확인 후 사용
5. 유의점
- 휴대폰 번호 인증, 결제 정보 등록 여부 확인
- 무료 사용량 및 사용량 제한 확인
- **License** 정보 확인
  - 변형 및 상업적 사용 가능 여부 등

## 등록
- 환경변수; **Shell** 문서에 작성하여 필요할 때 호출
- 식별하기 쉽도록 제일 아래에 작성
- `API KEY 이름`을 기준으로 호출

```bash
vim ~/.zshrc # 문서작성기/shell 문서 directory
# i : 작성 모드
export "API KEY 이름"="본인의_API_KEY" # 작성
# esc : 작성 종료
# : 명령어 입력 모드
# wq : 저장/종료
source ~/.zshrc 
# 적용
```

## 확인 및 호출
- 터미널에서 확인

```bash
echo $"API KEY 이름"
```

- **Python** 에서 호출
  - **API KEY**가 코드에 직접 저장되지 않고 변수명으로 저장됨
  - **OpenAI** : `client = OpenAI()` 선언으로 호출
    - 특정 키를 사용하고 싶은 경우 `openai.api_key = "사용할_API_KEY"`

```py
import os 
api_key = os.environ.get('API KEY 이름')
```
[¶ Top](#api-drill)

# API 호출 및 활용

## GPT-4o

### API 호출

```py
from openai import OpenAI
client = OpenAI()
```

### Prompt 작성
- 모델에게 역할을 부여하여 적합한 답변을 유도
- 사용자 정보를 입력하여 사용자에게 맞는 답변을 유도

```py
# 기본적인 프로그램 틀
system_message = {
  "role": "system",
  "content":"너는 변호사야, 나에게 법률적인 상담을 해줘."
}
# messages =[system_message]
# 메시지를 저장 할 공간
# 사용자 정보 추가 
messages = [system_message, {"role" : "user",
                            "content" : " 내 이름은 Polaris08"},
                            {"role" : "user",
                             "content" : "직업은 학생"},
                             {"role" : "user",
                              "content" : "컴퓨터 공학을 좋아함"}]
```

### 모델 설정 및 조건 부여
- `"role" : "system"` : 설정, 역할 부여
- `"role" : "user"` : 사용자 요구
- `"role" : "assistant"` : 참고사항

```py
# 이전 대화를 바탕으로 대화가 이어지도록 반복문 작성
while True: 
  user_input = input("사용자 전달:")

  # 중단 코드
  if user_input == "exit": 
    print("대답: 즐거운 대화였습니다! 감사합니다!")
    break 

  # 질문 저장
  messages.append({"role" : "user", 
                   "content" : user_input})
  
  # 모델 설정
  completion = client.chat.completions.create(
    model = "gpt-4o",
    messages=messages
  )

  # 대답 생성
  reply = completion.choices[0].message.content
  print("대답: " + reply)

  # 대답 저장 - 이전 대화 내역을 인지하고 추가 답변
  messages.append({"role" : "assistant",
                   "content" : reply})
```

## Eleven Labs [¶](https://elevenlabs.io)
- 음성 생성 **API** 서비스
- **Text to Speech** : 음성 생성
- **Speech to Speech** : 더빙
- **Text to SFX** : 효과음 생성

### API 설정
- 환경 변수에서 호출

```py
import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

# api key 불러오기
api_key = os.environ.get('Eleven_Labs_API_KEY')
```

### 모델 설정
- `VOICE_ID` 선택한 음성 모델의 **ID** 를 입력
- `"stability"` : 음성의 안정성을 설정
- `"similarity_boost"`  : 음성의 유사성 설정
- `"style"` : 억양 등 

```py
# 결과 파일 설정
output_filename = "output_audio.mp3"

# 음성 모델 불러오기
url = "https://api.elevenlabs.io/v1/text-to-speech/ZJCNdZEjYwkOElxugmW2/stream"
# url = "https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

# 문장을 입력받습니다.
text = input("텍스트를 입력하세요: ")

# 음성 생성 요청을 보냅니다.
data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 1,
        "style": 1,
        "use_speaker_boost": True
    }
}
```

### 결과값 설정
- 음성 데이터를 **mp3** 파일로 변환
- `chunck` : 대용량 데이터를 **chunk** 단위로 끊어서 처리
- `b""` : **bytes** 클래스
  - 바이트들을 표현하는 클래스
  - 각 문자는 ASCII 코드를 갖는 문자로 처리
- `reponse.status_code` [¶](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
  - **1XX: Informational(정보 제공)** : 임시 응답, 현재 요청까지는 처리
  - **2XX: Success(성공)** : 클라이언트의 요청이 서버에서 성공적으로 처리
  - **3XX: Redirection(리다이렉션)** : 완전한 처리를 위해서 추가 동작이 필요한 경우
  - **4XX: Client Error(클라이언트 에러)** : 없는 페이지를 요청하는 등 클라이언트의 요청 메시지 내용이 잘못된 경우
  - **5XX: Server Error(서버 에러)** : 서버 사정으로 메시지 처리에 문제가 발생한 경우

```py
response = requests.post(url, json=data, headers=headers, stream=True)

if response.status_code == 200:
    # api 요청 성공 == 200
    audio_content = b""

    # 청크 단위로 데이터 처리 - 대용량 데이터 처리 시
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_content += chunk

    segment = AudioSegment.from_mp3(io.BytesIO(audio_content))
    # 음성 데이터를 mp3 로 변환
    segment.export(output_filename, format="mp3")
    # mp3 파일로 저장
    print(f"Success! Wrote audio to {output_filename}")

    # 오디오를 재생합니다.
    play(segment)
else:
    print(f"Failed to save file: {response.status_code}")
```

### 오류 처리
- **mp3** 파일 재생 오류
  - **ffmpeg** 또는 **libav**가 시스템에 설치되어 있어야 **Pydub**가 MP3 파일을 읽을 수 있음

```bash
brew install ffmpeg
```

### 결과
- 입력 텍스트 : 가와바타 야스나리(川端康成), 「**설국**(雪国)」 도입부

> **국경의 긴 터널을 빠져나오자, 설국이었다.**  밤의 밑바닥이 하얘졌다. 신호소에 기차가 멈춰 섰다. 건너편 좌석의 여자가 일어서 다가오더니, 시마무라 앞의 유리창을 열어젖혔다. 눈의 냉기가 흘러들었다. 여자는 한껏 창 밖으로 몸을 내밀어 멀리 외치는 듯이, "역장니임, 역장니임ー" 등불을 들고 천천히 눈을 밟고 온 남자는 목도리를 콧등까지 두르고, 귀에 모자의 모피를 드리우고 있었다. -  《설국》 

- [음성 생성 결과 mp3 파일](https://drive.google.com/file/d/1DcqwV6a8cuiMW3pErkClI7djG7C2xz4M/view?usp=share_link)
  -  HYUK : 한국어 음성 모델 최상단

[¶ Top](#api-drill)

