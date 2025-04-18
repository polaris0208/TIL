## Django 미들웨어
- **Django** 애플리케이션의 입력 또는 출력을 전역적으로 변경하기 위한 프레임워크

### `settings.py`
- 순서가 중요
  - 요청과 응답은 미들웨어를 순차적으로 통과
  - 미들웨어에 의존성을 고려하여 순서 설정

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ...
]
```

### 작동방식
- 나열된 순서대로 **HttpRequest** 처리.
  - 각 미들웨어의 `process_request(), process_view()` 메서드 실행
- `View`에서 로직 실행
- 응답은 역순으로 미들웨어 통과하며 `process_response()` 메서드 실행

## 커스텀 미들웨어 작성
- 클래스형, 함수형으로 작성

### 함수 기반 미들웨어
- 간단한 로직 구현에 적합

```py
# custom_middleware.py
from time import process_time_ns

def view_process_time_middleware(get_response):
    def middleware(request):
        start_time = process_time_ns()
        response = get_response(request)
        end_time = process_time_ns()

        # 처리 시간을 응답 헤더에 추가
        if not response.has_header("View-Process-Run-Time"):
            response["View-Process-Run-Time"] = end_time - start_time
        return response

    return middleware
```

#### 등록

```yml
MIDDLEWARE = [
    ...
    'path.to.custom_middleware.view_process_time_middleware',
]
```

### 클래스 기반 미들웨어
- 확장성이 높아 복잡한 로직 구현에 적합
- 구조화된 형태로 추가 메서드 정의 가능

```py
# custom_middleware.py
from time import process_time_ns

class ViewProcessTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = process_time_ns()
        response = self.get_response(request)
        end_time = process_time_ns()

        if not response.has_header("View-Process-Run-Time"):
            response["View-Process-Run-Time"] = end_time - start_time

        return response
```

### 미들웨어 훅

#### 정의 가능 메서드
- `process_view(request, view_func, view_args, view_kwargs):`
  - 뷰 호출 직전에 실행
  - 요청 수정 또는 `HttpResponse` 반환으로 뷰 우회 가능
- `process_exception(request, exception):`
  - 뷰에서 예외 발생 시 호출.
  - 예외 처리 또는 `HttpResponse` 반환 가능
- `process_template_response(request, response):`
  - 응답이 `TemplateResponse`일 경우 호출
  - 템플릿 또는 컨텍스트 수정 가능

```py
class CustomHookMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("뷰 실행 전")
        return None  # 다음 미들웨어 또는 뷰로 계속 진행

    def process_exception(self, request, exception):
        print("예외 발생:", exception)
        return None  # 기본 예외 처리를 계속 진행

    def process_template_response(self, request, response):
        if hasattr(response, 'template_name'):
            response.context_data['extra_data'] = '미들웨어에서 추가된 데이터'
        return response

    def __call__(self, request):
        response = self.get_response(request)
        return response
```