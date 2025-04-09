# Slack Bolt 챗봇

## 준비물
- Slack 워크스페이스
- Slack App (Bot Token 포함)
- Python 환경 (예: VS Code)
- `bolt-python` 라이브러리 설치
- ngrok (테스트용)

## Slack App 생성
- [Slack API](https://api.slack.com/apps) → "Create New App"
- From scratch 선택 → App 이름 + 워크스페이스 지정

## 권한 설정 (OAuth & Permissions)
- `OAuth & Permissions` 탭
- Scopes에 아래 권한 추가:
  - `app_mentions:read`
  - `chat:write`
- 앱을 워크스페이스에 설치 후 **Bot Token (xoxb-...)** 복사

## 이벤트 구독 설정
- `Event Subscriptions` → Enable
- Request URL: `https://<ngrok-url>/slack/events`
- Subscribe to bot events:
  - `app_mention`

## Python 환경 설정

### pip 패키지 설치

```bash
pip install slack_bolt
```

---

## Bolt 앱 코드 작성

```python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os

# 환경변수로부터 토큰 불러오기
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# 이벤트 핸들러 등록
@app.event("app_mention")
def handle_app_mention(event, say):
    user = event["user"]
    say(f"<@{user}> 안녕하세요! Bolt 기반 챗봇입니다.")

# 실행
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
```

## 환경 변수 설정

```bash
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_APP_TOKEN="xapp-..."  # Socket Mode Token
```

> Socket Mode 사용 시 App Token은 **Connections > Socket Mode**에서 활성화 후 발급

## 실행 및 테스트

```bash
python app.py
```

- Slack 채널에서 `@봇이름` 멘션 시 응답 확인

---

## Bolt 특징 요약
- 공식 지원 Python 프레임워크
- Flask 없이 단독 실행 가능
- `say()` 함수로 메시지 응답 간편
- 다양한 이벤트 핸들러 지원 (`message`, `reaction_added` 등)

---

## 참고자료
- [Bolt for Python 공식 문서](https://slack.dev/bolt-python)
- [Socket Mode 소개](https://api.slack.com/apis/connections/socket)