# API 문서
> **API** 사용 설명, 사용되는 인자, 결과, 오류 처리 등

## 개념

- **API**를 사용하는 방법 및 결과, 발생 가능한 오류에 대한 상세한 설명 제공
  - 해당 문서를 바탕으로 프론트엔드에 적용


|요청|인증|엔드포인트|인자|결과|오류|
|-|-|-|-|-|-|
|POST|User|~/accounts/login/|username, password|token|vaild error|

## 종류
- 정해진 형식, 도구는 없음

### 노션(Notion)
- 업무 소통 도구
- 검색, 필터 정렬 등 데이터 작성

### 포스트맨(Postman)
- 태스트 및 결과를 그대로 반영하여 작성 가능
- 2인 초과 시 유료
- 버그 또는 오류가 종종 발생하여 저장되지 않는 경우 존재

### etc
- **Git book**
- 엑셀, 워드

## Django REST Framework
- **Swagger-UI / Redoc** 기반 툴 제공
  - 코드를 기반으로 API Doc을 만들고, 이 문서를 사용자가 보기 편하게 UI로 변환하는 도구
- `drf-spectacular` : **OpenAPI** 3 기반
- `drf-yasg` : **OpenAPI** 2 기반
  - 업데이트 중지
- **OpenAPI**
  - **OAS(OpenAPI Specification)**
  - 사용자 또는 프로그램이 소스코드나 글로 작성된 문서를 보지 않고도 서비스의 기능들을 이해할 수 있도록 **JSON** 형태로 표현하려는 프로젝트

### DRF-Spectacular
- `drf-yasg` 보다 최신  **OpenAPI** 기반
- 업데이트 유지중

#### 설치
- `pip install drf-spectacular`
- `settings.py` 등록
  - **App** 등록
  - **REST Framework** 등록
  - **DRF Spectacular** 설정 등록

```py
INSTALLED_APPS = [
    ...
    'drf_spectacular',
]

...

REST_FRAMEWORK = {
    ...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

...

SPECTACULAR_SETTINGS = {
    'TITLE': 'MY Django API',
    'DESCRIPTION': 'Django DRF API Doc',
    'VERSION': '1.0.0',
    ...
}
```

#### 기본 사용
- `urls.py` : 프로젝트 파일
- `~/api/schema/swagger-ui/` 에 접속해 문서 확인

```py
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS
    ...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

#### 커스텀
- `@extend_schema` : 클래스형 뷰, 요청 함수 앞에 붙여 사용
- `tags`, `description` : 분류 및 설명 추가
- `request` : 문서에 테스트 기능 추가

```py
class ArticleListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Articles"],
        description="Article 목록 조회를 위한 API",
    )
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["Articles"],
        description="Article 생성을 위한 API",
        request=ArticleSerializer,
    )
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## 결론
> **정해진 방법은 없다.**
- 노션, 엑셀등의 도구가 상황에 따라 전문적인 도구보다 유효할 수 있음
  - **API** 구현이 우선
  - **API** 문서를 작성하기 위해 과도한 학습이 요구되면 안됨
  - 인원변동이 잦은 업무환경일 경우 매번 **API**문서 도구 사용법을 익히는 것이 비효율적

