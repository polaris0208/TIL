# Redis 
> **Remote Dictionary Server**

## 개념
- 외부에 있는 `key-value`를 저장하는 서버
- 캐싱이나 세션관리 등에 자주 사용
- 인-메모리(**In-memory**) 데이터베이스
  - **Disk**에 비해 약 1,000배 이상 빠른 속도

### 필요성
- 조회수, 방문자수, 좋아요/팔로우 등
  - 동시 다발적, 빈번하게 업데이트 되는 요소
  - **Redis**로 처리
  - 영속적인 저장이 필요할 때만 **DB**로 이동

### Caching
- 지속적으로 사용하는 데이터
- 미리 불러온 뒤 **Redis**에 저장

## Strategy

### Read Cache Strategy

#### Look Aside(Cache Aside) 패턴

1. 캐시를 먼저 조회
2. 캐시가 없으면 DB를 조회

- 기본 캐시 전략
- 캐시와 DB가 분산되어 운용
  - **Redis가**에 문제가 생겨도 서비스에 문제가 없음
    - 다만 요청이 한번에 **DB**로 몰리면 서비스 장애 가능성 있음
- **Cache Warming** 최초에 캐시로 데이터를 넣어주는 작업

#### Read Through 패턴

- **Look Aside**와 비슷하지만 캐시만 바라보고 데이터를 조회
- 캐싱하는 로직은 다른 라이브러리에게 위임
  - 자동으로 **DB**와의 데이터 동기화
- 캐싱을 적극적으로 이용
  - **Redis**가 다운될 경우 서비스 중지

### 캐시 쓰기 전략 (Write Cache Strategy)

#### Write Back(Write Behind) 패턴
- 바로 **DB**에 저장하는 것이 아닌 캐시에 모아 두었다가 한 번에 저장
  - **bulk create** 하는것이 더 빠름
- 캐시에서 장애가 발생할 시 데이터 누락의 가능성이 있음

#### Write Through 패턴
- 데이터를 캐시에도 저장하고, DB에도 저장하는 방식
  - 캐시를 이용해서 **DB**를 동기화
  - 캐시의 데이터가 항상 최신 데이터로 유지됨
  - 두번의 저장이 이루어지기 때문에 데이터 유실에 민감한 로직에 사용

#### Write Around 패턴
- 모든 데이터는 **DB** 바로 저장
- **cache miss**가 발생했을때만 캐시와 **DB**에 저장
- 캐시와 DB간 데이터 불일치 가능성
    - **cache miss**가 발생하기 전까지의 수정 내용은 서비스에 반영되지 않음 
    - **cache**의 만료시간(**TTL**)을 짧게 잡고 사용

## 설치
- `brew install redis`
- `redis-server`
- `redis-cli`
  - `ping` : 테스트

### `redis-cli` Read
- `keys *` : 모든 **key** 조회
  - 사용 전 주의
    - 상품 데이터와 같은 경우
    - 항목이 매우 많기 때문에 큰 부하가 걸림
​
- `get <key>` : **Key**에 해당하는 **value** 조회
​

### `redis-cli` Create
- `set <key> <value>` : **key value** 저장
​- `setex <key> <seconds> <value>` : **seconds**초 뒤에 삭제되는 **key** **value**를 저장
​
### `redis-cli` Update
- `rename <key> <newkey>` : **key** 이름 변경
- `expire <key> <seconds>` : 해당 **Key**의 데이터 만료시간을 **seconds**초로 설정
​
### `redis-cli` Delete
- `del key1` : **key** 삭제
  - `[key2 ...]` 

## Django
- 기본적으로 시스템 메모리 사용
- **Local Cache**
  - 서버 컴퓨터의 자원을 사용해서 각 서버에 캐시를 저장
  - 서버 내에서 동작하기 때문에 속도가 빠름 
  - 서버 수가 늘어날수록 캐시 동기화를 위해 추가 리소스가 소모

```py
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def product_list(request):
    cache_key = "product_list"

    if not cache.get(cache_key):
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_data = serializer.data
        cache.set(cache_key, json_data, 10)

    response_data = cache.get(cache_key)
    return Response(response_data)
```

### Django Redis
- 기본 **cache** 기능에 **redis** 적용
- `pip install django-redis`
- `settings.py`에 등록
- `redis server` : 서버 실행
  - `keys *` : 검색
  - `<key_prefix> : <version> : <key>` 형식으로 키 등록

```py
...
CACHES = {  
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
...
```