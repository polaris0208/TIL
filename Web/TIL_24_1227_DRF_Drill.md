## INDEX
### 1. 프로젝트 개요 [¶](#프로젝트-개요)
### 2. App 설명 [¶](#app-설명)
### 3. API 문서 [¶](#api-문서)
### 4. 트러블 슈팅 [¶](#트러블-슈팅)

<hr>

## 프로젝트 개요
> **Django** 프레임워크를 이용한 상품 페이지 구현

### 프로젝트 실행

#### Docker 사용
- 자동화
  - `migration`
  - `superuser` 생성
  - `seed` 생성
  - `runserver` 진행

```bash
git clone https://github.com/polaris0208/django_assignment
docker-compose up --build
```

#### Python 사용
- `Mac OS` : `python3` 시도

```bash
git clone https://github.com/polaris0208/django_assignment
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### 카테고리 추가
- 카테고리는 관리자만 추가 가능
- `/admin` 에 접속하여 추가

### 구현 기능

#### accounts [¶](#accounts-기능)
> 계정 관련 기능
- 로그인/로그아웃 기능
- 회원 정보 기능
  - 회원가입/탈퇴 기능
  - 회원정보 수정/비밀번호 변경 기능
- 프로필 기능
  - 프로필 사진
  - 팔로우 기능

#### products [¶](#products-기능)
> 상품 관련 기능
- 상품 관리 기능
  - 상품 등록/수정/삭제 기능
  - 좋아요/찜 기능
  - 해시태그 기능

### 프로젝트 구조

```
drf_assignment/
│
├── README.md : 프로젝트 설명
├── requirements.txt : 의존성 목록
├── .gitignore : 버전관리 제외 목록
├── .dockerignore : 도커 실행 시 제외 목록
├── Dockerfile : 컨테이너 생성 설정
├── docker-compose.yml : 컨테이너 실행 설정
│
├── manage.py : 프로젝트 관리 파일
├── spartamarket/ : 프로젝트 앱
├── media/ : 동적 자원 경로
│
├── accounts/ : 계정 앱
└── products/ : 상품 앱
```

### ERD
![ERD](/IMG/ERD2.png)
- **User**
  - **User ↔ Products**
    - **1:N** : 하나의 사용자에 여러 상품이 있을 수 있음
  - **User ↔ Products** 좋아요/찜
    - **M:N** : 사용자가 여러 상품을 좋아요할 수 있음
  - **User ↔ User** 팔로우/팔로워
    - **M:N** : 사용자가 다른 사용자들을 팔로우할 수 있고, 다른 사용자는 그들을 팔로우할 수 있음

- **Products**
  - **Products ↔ HashTag**
    - **M:N** : 여러 해시태그와 여러 상품이 연결될 수 있음

## 프로젝트 기본 설정

### `settngs.py`
- `third_party` : **API** 테스트 도구
- `REST_FRAMEWORK` 
  - **API** 인증 전역 설정 : 전체 기본 설정
    - 로그인/**JWT**
  - 페이지네이션 전역설정
- `SIMPLE_JWT` : **JWT** 토큰 설정
- `SPECTACULAR_SETTINGS` : **OpenAPI** `drf_spectacular` 설정
- 시간대/동적 자원 경로 설정

```py 
...
INSTALLED_APPS = [
    ...
    # DRF
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    # local
    'accounts',
    'products',
    # third_party
    'django_seed',
    'drf_spectacular',
    ...
]
...
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
...
# User 모델 설정
AUTH_USER_MODEL = 'accounts.User'

# JWT 인증
REST_FRAMEWORK = {
    # API에 인증 전역 설정
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # drf-spectacular
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # pagenation
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE' : 5,  # 페이지당 보여줄 개수
}

# JWT 설정
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# SPECTACULAR 설정
SPECTACULAR_SETTINGS = {
    'TITLE': 'SpartaMarket',
    'DESCRIPTION': 'DRF API Doc',
    'VERSION': '1.0.0',
    'COMPONENT_SPLIT_REQUEST': True
}


# 미디어 파일 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

### `urls.py`
- 앱 경로 등록
- 동적 자원 경로 등록
- `api/schema/swagger-ui/` : **API** 테스트 경로

```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("products/", include("products.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
```

## accounts 기능

### `models.py`
- `CustomUserManager` : 사용자 모델의 매니저
    - 기본 매니저를 상속 받아 기능 수정
    - 이메일 필수 설정
    - 관리자 계정 생성 설정
- `User` : 사용자 모델
    - 로그인 시 이메일 사용
- `Follow` : **N:M** 관계 중간 테이블
    - `unique_together` 중복 방지

```py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일은 필수입니다")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField("이메일", unique=True)
    username = models.CharField("닉네임", max_length=150, unique=True)
    profile_image = models.ImageField(
        "프로필 이미지", default='profile/default.png', upload_to="profile/", blank=True, null=True
    )

    followings = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",  # 역참조 이름
        through="Follow",  # 중간 테이블
        blank=True,
    )

    USERNAME_FIELD = "email"  # 로그인 시 이메일 사용
    REQUIRED_FIELDS = []  # 기본값 email

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# 중간 테이블
class Follow(models.Model):
    follower = models.ForeignKey(
        User, related_name="followed_users", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, related_name="following_users", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")  # 중복 팔로우 방지

    def __str__(self):
        return f"{self.follower} follows {self.following}"
```

### `serializers.py`

```py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError

User = get_user_model()
```

#### 회원가입 기능
- `password2` : 비밀번호 입력 확인 용도, **DB**에 반영되지 않음

```py
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "password", "password2", "username", "profile_image")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "비밀번호 불일치"})
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)
```

#### 프로필 기능
- `read_only=True`
    - `follow` 관련 기능은 별도의 로직으로 작동
    - 일기 전용으로 설정

```py
class UserProfileSerializer(serializers.ModelSerializer):

    class FollowSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("id", "email", "username", "profile_image")

    followers = FollowSerializer(many=True, read_only=True)
    followings = FollowSerializer(many=True, read_only=True)
    follower_count = serializers.IntegerField(source="followers.count", read_only=True)
    following_count = serializers.IntegerField(
        source="followings.count", read_only=True
    )
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "profile_image",
            "followings",
            "followers",
            "follower_count",
            "following_count",
        ]

    def get_profile_image(self, obj):
        request = self.context.get("request")
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return None
```

#### 회원정보 수정 기능
- `write_only=True` : 비밀번호는 확인 불가능
- `class PasswordChangeSerializer(serializers.Serializer):`
  - 기존 비밀번호/새로운 비밀번호 입력
  - 기존 비밀번호 정당성 평가
  - 새로운 비밀번호 동일성 평가

```py
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "profile_image")


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    # 현재 비밀번호 확인
    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise ValidationError("올바르지 않은 비밀번호")
        return value

    # 새 비밀번호 확인
    def validate_new_password(self, value):
        user = self.context["request"].user
        if user.check_password(value):
            raise ValidationError("동일한 비밀번호")

        try:
            validate_password(value)
        except ValidationError as e:
            raise ValidationError(f'유효하지 않은 비밀번호 : {", ".join(e.messages)}')

        return value

    def save(self):
        user = self.context["request"].user
        new_password = self.validated_data["new_password"]
        user.set_password(new_password)
        user.save()
```

### `views.py`

```py
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    SignupSerializer,
    UserUpdateSerializer,
    UserProfileSerializer,
    PasswordChangeSerializer,
)
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import OpenApiExample

User = get_user_model()
```

#### 회원가입/탈퇴 기능
- `@authentication_classes([])` : 전역 인증 설정 무시
- `@permission_classes([AllowAny])` : 전역 `IsAuthenticated` 설정 무시
- `def resign(request):` : **JWT** 토큰으로 인증 후 비밀번호로 한번 더 확인


```py
@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "회원가입 성공"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])  # 인증이 필요한 경우 인증 클래스 추가
@permission_classes([IsAuthenticated])  # 로그인된 사용자만 접근 가능
def resign(request):
    password = request.data.get("password")  # 요청 데이터에서 비밀번호 받기
    user = request.user  # 현재 요청을 보낸 사용자 정보

    # 비밀번호 확인
    user = authenticate(email=user.email, password=password)
    if user is None:
        return Response(
            {"message": "비밀번호가 일치하지 않습니다."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        # 비밀번호가 일치하면 계정 삭제
        user.delete()
        return Response(
            {"message": "회원 탈퇴가 완료되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )
    except User.DoesNotExist:
        return Response(
            {"message": "사용자를 찾을 수 없습니다."},
            status=status.HTTP_400_BAD_REQUEST,
        )
```

#### 로그인/로그아웃 기능
- `def login(request):` : 이메일/비밀번호 화인 후 **JWT** 토큰 발급
- `def logout(request):` : `refresh` 토큰 블랙리스트 처리하여 로그아웃

```py
@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    user = authenticate(request, email=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return JsonResponse(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "message": "로그인 성공",
            },
            status=200,
        )
    else:
        return JsonResponse({"error": "올바르지 않은 이메일"}, status=400)


@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def logout(request):
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "로그아웃 성공"})
    except Exception:
        return Response({"error": "로그아웃 실패"}, status=status.HTTP_400_BAD_REQUEST)
```

#### 회원정보 조회/수정 기능
- `partial=True` : 일부 수정 허용

```py
@api_view(["GET", "PUT", "PATCH"])
def profile(request):
    user = request.user

    if request.method == "GET":
        serializer = UserProfileSerializer(user, context={"request": request})
        return Response(serializer.data, status=200)

    if request.method in ("PUT", "PATCH"):
        serializer = UserUpdateSerializer(
            instance=user, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "회원정보 수정 성공",
                    "user": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "비밀번호 변경 성공"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

#### 팔로우
- `if me == profile_user:` : 본인 여부 확인
- `if me.followings.filter(pk=profile_user.pk).exists():` : 팔로우 여부 확인

```py
@api_view(["POST"])
def follow(request, user_pk):
    profile_user = get_object_or_404(User, pk=user_pk)
    me = request.user

    if me == profile_user:
        return Response(
            {"error": "자신은 팔로우 불가"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if me.followings.filter(pk=profile_user.pk).exists():
        me.followings.remove(profile_user)
        is_followed = False
        message = f"{profile_user.email} 팔로우 취소"
    else:
        me.followings.add(profile_user)
        is_followed = True
        message = f"{profile_user.email} 팔로우"

    return Response(
        {
            "is_followed": is_followed,
            "message": message,
        },
        status=status.HTTP_200_OK,
    )
```

### `urls.py`
- `tocken/~` : **JWT** 토큰 생성 관련

```py
from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("resign/", views.resign, name="resign"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
]

urlpatterns += [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]

from .views import ChangePasswordView

urlpatterns += [
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
```

<hr>

## products 기능

### `models.py`

#### 카테고리/해시태그
- `def extract_hashtags(content):`
    - 해시태그 추출 함수
    - `#` 뒤에오는 숫자/영어/한글 추출

```py
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import re

def extract_hashtags(content):
    hashtags = re.findall(r"#([0-9a-zA-Z가-힣_]+)", content)  # # 뒤에 오는 단어들 찾기
    return hashtags

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

def products_image_path(instance, filename):
    return f"products/{instance.user.username}/{filename}"

def validation_hashtag(value):
    if not re.match(r"^[0-9a-zA-Z가-힣_]+$", value):
        raise ValidationError("올바르지 않은 해시태그 형식.")

class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[validation_hashtag])

    def __str__(self):
        return f"#{self.name}"
```

#### 상품 모델
- `if self.author == user:` : 좋아요/찜 본인 여부 확인
- `def save(self, *args, **kwargs):`
    - `content`에서 해시태그 추출

```py
class Products(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to=products_image_path, blank=True, null=True)
    like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="like_products",
        blank=True
    )
    hashtags = models.ManyToManyField(HashTag, related_name='products', blank=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True)

    def __str__(self):
        return self.title

    @property
    def like_user_counter(self):
        return self.like_user.count()

    def view_counter(self):
        self.views += 1
        self.save()
        return self.views

    def add_like(self, user):
        if self.author == user:
            raise ValidationError("자신의 상품은 좋아요/찜 불가")
        self.like_user.add(user)

    def remove_like(self, user):
        if self.author == user:
            raise ValidationError("자신의 상품은 좋아요/찜 취소 불가.")
        self.like_user.remove(user)

    def save(self, *args, **kwargs):
        # 해시태그 자동 추출
        hashtags = extract_hashtags(self.content)  # content에서 해시태그 추출
        hashtag_objects = []
        
        # 해시태그 객체가 없으면 생성하여 리스트에 추가
        for hashtag in hashtags:
            hashtag_obj, created = HashTag.objects.get_or_create(name=hashtag)
            hashtag_objects.append(hashtag_obj)
        
        # 먼저 객체를 저장
        super().save(*args, **kwargs)
        
        # 그 후에 해시태그 연결
        self.hashtags.set(hashtag_objects)
```

### `serializers.py`
- `작성자 / 해시태그 / 좋아요/찜 / 조회수` : 별도의 로직으로 동작
    - 직렬화 대상에서 제거
    - 별도의 작업 과정으로 저장

```py
from rest_framework import serializers
from .models import Category, HashTag, Products, extract_hashtags

class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ['id', 'name']  # id와 name을 반환

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # id와 name을 반환

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    like_user_counter = serializers.ReadOnlyField()
    hashtags = HashTagSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all()) # Post에만 작동 / DB에 간섭

    class Meta:
        model = Products
        exclude = ['like_user', 'views']  # 'views'와 'like_user'는 직렬화에서 제외

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 'request'가 context에 존재하는지 확인
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.fields.pop('hashtags', None)

    def create(self, validated_data):
        # 새로운 상품을 생성할 때 현재 사용자 자동 설정
        validated_data['author'] = self.context['request'].user  # 요청한 사용자가 author로 자동 설정
        validated_data['views'] = 0  # 조회수 초기값 설정 (상품 생성 시 자동으로 0으로 설정)
        product = super().create(validated_data)
        
        # 해시태그 자동 추출 처리
        hashtags = extract_hashtags(product.content)  # content에서 해시태그 추출
        hashtag_objects = []
        for hashtag in hashtags:
            hashtag_obj, created = HashTag.objects.get_or_create(name=hashtag)
            hashtag_objects.append(hashtag_obj)
        product.hashtags.set(hashtag_objects)  # 해시태그 연결
        product.save()

        return product

    def update(self, instance, validated_data):
        # 기존 상품 수정 시 작성자 정보, 해시태그, 조회수, 좋아요는 수정하지 않음
        validated_data.pop('author', None)
        validated_data.pop('hashtags', None)  # 해시태그 수정은 제외
        validated_data.pop('views', None)
        validated_data.pop('like_user', None)

        # 상품을 업데이트한 후, 해시태그 자동 추출
        instance = super().update(instance, validated_data)
        
        # content에서 해시태그 추출 및 업데이트
        hashtags = extract_hashtags(instance.content)  # content에서 해시태그 추출
        hashtag_objects = []
        for hashtag in hashtags:
            hashtag_obj, created = HashTag.objects.get_or_create(name=hashtag)
            hashtag_objects.append(hashtag_obj)
        
        instance.hashtags.set(hashtag_objects)  # 해시태그 연결
        instance.save()

        return instance
```

### `views.py`

```py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404  # 추가: get_object_or_404 임포트
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination
```

#### 상품 조회 기능
- `paginator` : 페이지네이션 설정
    - 5개의 게시물당 한 페이지 생성
    - `?page=<int:page_number>`로 접속

```py
class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # 인증된 사용자만 접근 가능
    
    def get(self, request):
        # 모든 상품 목록 조회
        products = Products.objects.all().order_by("-created_at")

        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        # 새로운 상품 생성
        serializer = ProductSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()  # 자동으로 author가 현재 사용자로 설정됨
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

#### 상품 상세 기능
- `if product.author != request.user:` : 수정/삭제 시 본인 여부 확인

```py
class ProductDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # 인증된 사용자만 접근 가능

    def get(self, request, pk):
        # 특정 상품 조회 및 조회수 증가
        product = get_object_or_404(Products, pk=pk)  # get_object_or_404 사용

        # 조회수 증가
        views = product.view_counter()

        # 상품 정보를 반환
        serializer = ProductSerializer(product)
        return Response({"product": serializer.data, "views": views})

    def put(self, request, pk):
        # 상품 정보 수정
        product = get_object_or_404(Products, pk=pk)  # get_object_or_404 사용

        # 상품 수정 권한 체크 (자신의 상품만 수정 가능)
        if product.author != request.user:
            return Response(
                {"detail": "권한이 없습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # 상품 삭제
        product = get_object_or_404(Products, pk=pk)  # get_object_or_404 사용

        # 상품 삭제 권한 체크 (자신의 상품만 삭제 가능)
        if product.author != request.user:
            return Response(
                {"detail": "권한이 없습니다."},
                status=status.HTTP_403_FORBIDDEN,
            )

        product.delete()
        return Response(
            {"detail": "상품이 삭제되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )
```

#### 상품 좋아요/찜 기능
- `if product.author != request.user:` : 좋아요/찜 추가/삭제 시 본인 여부 확인

```py
class ProductLikeView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def post(self, request, pk):
        # 좋아요 추가
        product = get_object_or_404(Products, pk=pk)  # get_object_or_404 사용

        # 자신이 작성한 상품에는 좋아요를 추가할 수 없음
        if product.author == request.user:
            return Response(
                {"detail": "자신의 상품은 좋아요/찜 불가."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product.add_like(request.user)
        return Response({"detail": "상품 좋아요/찜 성공."}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        # 좋아요 제거
        product = get_object_or_404(Products, pk=pk)  # get_object_or_404 사용

        # 자신이 작성한 상품에는 좋아요를 제거할 수 없음
        if product.author == request.user:
            return Response(
                {"detail": "자신의 상품은 좋아요/찜 불가."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        product.remove_like(request.user)
        return Response({"detail": "상품 좋아요/찜 취소."}, status=status.HTTP_200_OK)
```

#### 카테고리 조회 기능

```py
class CategoryListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        categories = Category.objects.all()  # 모든 카테고리 가져오기
        serializer = CategorySerializer(categories, many=True)  # 직렬화
        return Response(serializer.data, status=status.HTTP_200_OK)
```

### `urls.py`

```py
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductLikeView, CategoryListView

app_name = "products"
urlpatterns = [
    path('', ProductListCreateView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/like/', ProductLikeView.as_view(), name='like'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
```

### `admin.py`
- 상품, 카테고리를 관리자 관리 항목에 추가

```py
from django.contrib import admin
from .models import Products, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "quantity", "category"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
```

<hr>

# API 문서

## 1. acccounts [¶](#accounts)
## 2. products [¶](#products)

<hr>

## accounts

|상세|내용|유형|URL|
|:---|:---|:---|:---|
|[¶](#회원가입)|회원가입|POST|`accounts/signup/`|
|[¶](#회원-탈퇴)|회원 탈퇴|DELETE|`accounts/resign/`|
|[¶](#로그인)|로그인|POST|`accounts/login/`|
|[¶](#로그아웃)|로그아웃|POST|`accounts/logout/`|
|[¶](#프로필-조회)|프로필 조회|GET|`accounts/profile/`|
|[¶](#프로필-수정)|프로필 수정|PUT / PATCH|`accounts/profile/`|
|[¶](#비밀번호-변경)|비밀번호 변경|POST|`accounts/change-password/`|
|[¶](#팔로우)|팔로우|POST|`accounts/<int:user_pk>/follow/`|


<hr>

### 회원가입

|[¶](#accounts)|회원가입|POST|AllowAny|-|-|`accounts/signup/`|-|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|-|Json|

- **Body**
    - `email` : 고유한 값, 로그인에 사용
    - `password2`
    - `password`와 동일하게 입력
    - 확인용 / 저장되지 않는 값
    - `username` : 고유한 값

    ```json
    {
        "email": "test@example.com",
        "password": "qwer1234!@",
        "password2": "qwer1234!@",
        "username": "testuser"
    }
    ```

#### Response

#### 성공 : 201 Created

```json
{"message": "회원가입 성공"}
```

#### 실패 : 400 Bad Request

```json
{"email": ["이 필드는 필수 항목입니다."]}
```

```json
{"username": ["사용자의 닉네임은/는 이미 존재합니다."]}
```

```json
{"password": ["비밀번호 불일치"]}
```

<hr>

### 회원 탈퇴

|[¶](#accounts)|회원탈퇴|DELETE|JWT|Authenticated|access|`accounts/resign/`|-|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|Json|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGciOiJIUzI...`

- **Body**
    - `password` : 로그인된 상태에서 비밀번호만 확인

    ```json
    {"password": "qwer1234!@"}
    ```

#### 성공 : 204 No Content

```json
{"message": "회원 탈퇴가 완료되었습니다."}
```

#### 실패 : 400 Bad Request

```json
{"message": "비밀번호가 일치하지 않습니다."}
```

```json
{"message": "사용자를 찾을 수 없습니다."}
```

<hr>

### 로그인

|[¶](#accounts)|로그인|POST|AllowAny|-|-|`accounts/login/`|-|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|-|json|

- **Body**

```json
{
    "email" : "admin@example.com",
    "password" : "password"
}
```

#### 성공 : 200 OK

```json
{
    "access": "eyJhbGciO...",
    "refresh": "eyJhbGci...",
    "message": "로그인 성공"
}
```

#### 실패 : 400 Bad Request

```json
{"error": "올바르지 않은 이메일"}
```

<hr>v

### 로그아웃

|[¶](#accounts)|로그아웃|POST|AllowAny|-|refresh|`accounts/logout/`|-|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|refresh|-|

- **Auth**
    - **Bearer Token**
        - ` "refresh": "eyJhbGciOiJIUzI1NiIsInR5...`

#### 성공 : 200 OK

```json
{"message": "로그아웃 성공"}
```

#### 실패 : 400 Bad Request

```json
{"error": "로그아웃 실패"}
```

<hr>

### 프로필 조회

|[¶](#accounts)|조회|GET|JWT|Authenticated|access|`accounts/profile/`|본인|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGciOiJIUzI...`

#### 성공 : 200 OK

```json
{
    "email": "admin@example.com",
    "username": "",
    "profile_image": "http://127.0.0.1:8000/media/profile/default.png",
    "followings": [],
    "followers": [],
    "follower_count": 0,
    "following_count": 0
}
```

#### 실패 : 401 Bad Unauthorized

```json
{"detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."}
```

<hr>

### 프로필 수정

|[¶](#accounts)|수정|PUT / PATCH|JWT|Authenticated|access|`accounts/profile/`|본인|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|Json|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGciOiJIUzI...`
- **Body**
    - `username` : 이메일은 변경 불가능

    ```json
    {"username": "edittest"}
    ```


#### 성공 : 200 OK

```json
{
    "message": "회원정보 수정 성공",
    "user": {
        "username": "edittest",
        "profile_image": "/media/profile/default.png"
    }
}
```

#### 실패 : 401 Bad Unauthorized

```json
{"detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."}
```

<hr>

### 비밀번호 변경

|[¶](#accounts)|비밀번호 변경|POST|JWT|Authenticated|access|`accounts/change-password/`|본인|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|Json|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGciOiJIUzI...`
- **Body**
    - `password` : 로그인된 상태에서 비밀번호만 확인

    ```json
    {
        "old_password": "password",
        "new_password": "qwer12344"
    }
    ```


#### 성공 : 200 OK

```json
{"detail": "비밀번호 변경 성공"}
```

#### 실패 : 400 Bad Request

```json
{"old_password": ["올바르지 않은 비밀번호"]}
```

<hr>

### 팔로우

|[¶](#accounts)|팔로우|POST|JWT|Authenticated|access|`accounts/<int:user_pk>/follow/`|본인 제외|
|-|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGciOiJIUzI...`

#### 성공 : 200 OK

```json
{
    "is_followed": true,
    "message": "test@test.com 팔로우"
}
```

```json
{
    "is_followed": true,
    "message": "test@test.com 팔로우 취소"
}
```

#### 실패 : 400 Bad Request

```json
{"error": "자신은 팔로우 불가"}
```

```json
{"detail": "찾을 수 없습니다."}
```

<hr>

## products

|상세|내용|유형|URL|
|:---|:---|:---|:---|
|[¶](#상품-조회)|상품 조회|GET|`products/`|
|[¶](#상품-생성)|상품 생성|POST|`products/`|
|[¶](#상품-상세)|상품 상세|GET|`products/<int:pk>/`|
|[¶](#상품-수정)|상품 수정|PUT|`products/<int:pk>/`|
|[¶](#상품-제거)|상품 제거|DELETE|`products/<int:pk>/`|
|[¶](#상품-좋아요-찜)|상품 좋아요/찜|POST|`products/<int:pk>/like/`|
|[¶](#상품-좋아요-찜-취소)|상품 좋아요/찜 취소|DELETE|`products/<int:pk>/like/`|
|[¶](#카테고리-조회)|카테고리 조회|GET|`categories/`|

<hr>

### 상품 조회
-  `?page=<int:page_number>` : 페이지 이동

|[¶](#products)|조회|GET|Authenticated / ReadOnly|access / -|`products/`|-|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access / - |-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 200 OK

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "",
            "like_user_counter": 0,
            "hashtags": [
                {
                    "id": 1,
                    "name": "테스트"
                },
                {
                    "id": 2,
                    "name": "test"
                }
            ],
            "category": 1,
            "title": "새로운 상품",
            "content": "#테스트 #test 상품 설명",
            "created_at": "2024-12-26T21:39:09.136986+09:00",
            "updated_at": "2024-12-26T21:39:09.146829+09:00",
            "product_name": "상품 이름",
            "price": 2008,
            "quantity": 918,
            "image": null
        }
    ]
}
```

#### 실패 : 404 Not Found

```json
{"detail": "페이지가 유효하지 않습니다."}
```

<hr>

### 상품 생성

|[¶](#상품-생성)|생성|POST|Authenticated|access|`products/`|-|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|Json|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`
- **Body**
    - `email` : 고유한 값, 로그인에 사용
    - `password2`
    - `password`와 동일하게 입력
    - 확인용 / 저장되지 않는 값
    - `username` : 고유한 값

    ```json
    {
    "category": "1",
    "title": "새로운 상품",
    "content": "#테스트 #test 상품 설명",
    "product_name": "상품 이름",
    "price": 2008,
    "quantity": 918
    }
    ```

#### Response

#### 성공 : 201 Created

```json
{
    "id": 1,
    "author": "",
    "like_user_counter": 0,
    "category": 1,
    "title": "새로운 상품",
    "content": "#테스트 #test 상품 설명",
    "created_at": "2024-12-26T21:39:09.136986+09:00",
    "updated_at": "2024-12-26T21:39:09.146829+09:00",
    "product_name": "상품 이름",
    "price": 2008,
    "quantity": 918,
    "image": null
}
```

#### 실패 : 400 Bad Request

```json
{"category": ["이 필드는 필수 항목입니다."]}
```

#### 실패 : 401 Bad Unauthorized

```json
{"detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."}
```

<hr>

### 상품 상세

|[¶](#products)|상세|GET|Authenticated / ReadOnly|access / -|`products/<int:pk>/`|-|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access / -|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 200 OK

```json
{
    "product": {
        "id": 1,
        "author": "",
        "like_user_counter": 0,
        "hashtags": [
            {
                "id": 1,
                "name": "테스트"
            },
            {
                "id": 2,
                "name": "test"
            }
        ],
        "category": 1,
        "title": "새로운 상품",
        "content": "#테스트 #test 상품 설명",
        "created_at": "2024-12-26T21:39:09.136986+09:00",
        "updated_at": "2024-12-26T21:54:46.174871+09:00",
        "product_name": "상품 이름",
        "price": 2008,
        "quantity": 918,
        "image": null
    },
    "views": 1
}
```

#### 실패 : 404 Not Found

```json
{"detail": "찾을 수 없습니다."}
```

<hr>

### 상품 수정

|[¶](#products)|수정|PUT|Authenticated|access|`products/<int:pk>/`|본인|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|Json|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`
- **Body**
    - `email` : 고유한 값, 로그인에 사용
    - `password2`
    - `password`와 동일하게 입력
    - 확인용 / 저장되지 않는 값
    - `username` : 고유한 값

    ```json
    {
    "category": "1",
    "title": "수정된 상품",
    "content": "#수정 #update 상품 수정",
    "product_name": "수정된 상품 이름",
    "price": 1993,
    "quantity": 516
    }
    ```

#### Response

#### 성공 : 200 OK

```json
{
    "id": 1,
    "author": "",
    "like_user_counter": 0,
    "hashtags": [
        {
            "id": 3,
            "name": "수정"
        },
        {
            "id": 4,
            "name": "update"
        }
    ],
    "category": 1,
    "title": "수정된 상품",
    "content": "#수정 #update 상품 수정",
    "created_at": "2024-12-26T21:39:09.136986+09:00",
    "updated_at": "2024-12-26T22:01:12.345495+09:00",
    "product_name": "수정된 상품 이름",
    "price": 1993,
    "quantity": 516,
    "image": null
}
```

#### 실패 : 403 Forbidden

```json
{"detail": "권한이 없습니다."}
```

#### 실패 : 404 Not Found

```json
{"detail": "찾을 수 없습니다."}
```

<hr>

### 상품 제거

|[¶](#products)|제거|DELETE|Authenticated|access|`products/<int:pk>/`|본인|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 204 No Content

```json
{"detail": "상품이 삭제되었습니다."}
```

#### 실패 : 403 Forbidden

```json
{"detail": "권한이 없습니다."}
```

<hr>

### 상품 좋아요 찜

|[¶](#products)|좋아요/찜|POST|Authenticated|access|`products/<int:pk>/like/`|본인 제외|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 200 OK

```json
{"detail": "상품 좋아요/찜 성공."}
```

#### 실패 : 400 Bad Request

```json
{"detail": "자신의 상품은 좋아요/찜 불가."}
```

<hr>

### 상품 좋아요 찜 취소

|[¶](#products)|좋아요/찜 취소|DELETE|Authenticated|access|`products/<int:pk>/like/`|본인 제외|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 200 OK

```json
{"detail": "상품 좋아요/찜 취소."}
```

#### 실패 : 400 Bad Request

```json
{"detail": "자신의 상품은 좋아요/찜 불가."}
```

<hr>

### 카테고리 조회

|[¶](#products)|카테고리|GET|Authenticated / ReadOnly|access / -|`categories/`|-|
|-|-|-|-|-|-|-|

#### Request

|Auth|Body|
|-|-|
|access / -|-|

- **Auth**
    - **Bearer Token**
        - ` "access": "eyJhbGcieyJhb...`

#### Response

#### 성공 : 200 OK

```json
[{"id": 1, "name": "테스트"}]
```

## 트러블 슈팅

## 1. url 수정/추가 문제

### 문제
> 기능이 개발되는 과정에서 사용하는 **url**이 많아지고 수정하기 어려워지는 문제

### 해결

#### 복합 대입 연산자 활용
- 새로 추가되는 **url** 분리하여 관리

```py
from .views import ChangePasswordView

urlpatterns += [
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
```

## 2. 모델 수정 후 테스트 절차의 번거로움

### 문제
> 모델이 수정될 때마다 **DB** 초기화, `migrate` , 계정 생성 등의 작업에 시간 소요

### 해결

#### Docker 사용
- `migrate`, `createsuperuser`, 까지 자동수행
- `seed` 생성 제외
    - 게시물 생성은 카테고리 생성 후 진행해야 함

```yml
    ...
    environment:
      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_EMAIL: admin@example.com
      DJANGO_SUPERUSER_PASSWORD: password
    command: >
      sh -c "
      python manage.py makemigrations &&
      python manage.py migrate &&
      python manage.py createsuperuser --noinput || true &&
      python manage.py runserver 0.0.0.0:8000
      "
```

## 3. 해시태그 생성 오류

### 문제
> 한글로 작성한 경우 생성이 안되는 문제

### 해결

#### 조건에 한글 추가
- 한글 조건 추가 : `가-힣`
- 상품 설명에서 `#` 뒤에 붙은 `숫자/알파벳/한글` 을 추출하여 해시태그 생성

```py
def extract_hashtags(content):
    hashtags = re.findall(r"#([0-9a-zA-Z가-힣_]+)", content)  # # 뒤에 오는 단어들 찾기
    return hashtags

class Products(models.Model):
    ...
    hashtags = models.ManyToManyField(HashTag, related_name='products', blank=True)
    ...

    def save(self, *args, **kwargs):
            # 해시태그 자동 추출
            hashtags = extract_hashtags(self.content)  # content에서 해시태그 추출
            hashtag_objects = []
            
            # 해시태그 객체가 없으면 생성하여 리스트에 추가
            for hashtag in hashtags:
                hashtag_obj, created = HashTag.objects.get_or_create(name=hashtag)
                hashtag_objects.append(hashtag_obj)
            
            # 먼저 객체를 저장
            super().save(*args, **kwargs)
            
            # 그 후에 해시태그 연결
            self.hashtags.set(hashtag_objects)
```