# SSE, WebSocket, Celery

## SSE (Server-Sent Events)
- 클라이언트가 서버로부터 실시간 데이터를 받아오는 일방향 방식
- 단방향 통신
- 대부분의 최신 브라우저에서 지원됨.
- HTTP 프로토콜을 사용하므로 서버 설정이 간단

### Django

```python
# views.py

from django.http import HttpResponse
import time

def event_stream():
    while True:
        yield f"data: {time.time()}\n\n"
        time.sleep(1)

def sse_view(request):
    return HttpResponse(event_stream(), content_type='text/event-stream')
```

```py
# urls.py

from django.urls import path
from .views import sse_view

urlpatterns = [
    path('sse/', sse_view),
]
```

## WebSocket
- 클라이언트와 서버 간의 양방향 통신을 지원하는 프로토콜
- 양방향 통신
- HTTP 요청/응답에 비해 네트워크 리소스를 적게 사용


### Django
- ASGI 설정 파일을 수정하여 WebSocket 지원을 추가
- CHANNEL_LAYERS를 설정하여 Redis를 백엔드로 사용

#### Channels 설치

```bash
pip install channels
```

#### Consumer

```py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat'
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
```

```py
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),
]
```

## Celery
- 비동기 작업 큐 시스템으로
- Django에서 백그라운드 작업을 처리
- 시간이 오래 걸리는 작업을 백그라운드에서 처리
- 분산 시스템으로 쉽게 확장할 수 있어 대규모 작업을 처리할 때 유리

### 설치

```bash
pip install celery
pip install redis
```

### `celery.py`

```py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
```

### `settings.py`

```py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

### `task.py`

```py
from celery import shared_task

@shared_task
def send_email():
    # 이메일 전송 로직
    pass
```

### `views.py`

```py
...
send_email.delay()
...
```
