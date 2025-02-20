# 프로젝트 개요

# 🛎️서비스 명 : ReadRiddle

# 💡아이디어, 기획

이번 스파르타 과정에서 저희가 배웠던 여러가지 내용들을 복습하는데 활용하는 AI 챗봇을 개발하면 유용할 것 같다는 생각에, 해당 자료들을 바탕으로 AI가 퀴즈를 내고 사용자가 정답을 입력하면 이에 대해 피드백해주는 학습용 AI 모델을 개발하게 되었습니다.여기에 좀 더 확장성을 고려하여 오픈소스와 공식문서(Django, DRF, React) 를 참고자료(RAG)로 사용하는 QnA 용 AI 챗봇을 추가해서 퀴즈와 학습을 병행할 수 있도록 했습니다.

# ⚙️주 사용 기술

- **프론트엔드**
    
    React를 도입함으로써 REST API의 모든 메서드를 보다 효과적으로 활용하고자 하며, 
    프로젝트의 확장성과 유연성을 기대 Django DRF와의 연동에 최적화된 선택이라고 판단합니다.
    
    또한 자바스크립트 라이브러리로, 사용자 인터페이스(UI)를 구축하는 데 사용됩니다. 컴포넌트 기반 아키텍처를 통해 재사용 가능한 UI 컴포넌트를 쉽게 만들 수 있습니다.
    
    - JavaScript 기반
    - 다양한 데이터 전송 방식과 동적인 UI 구현에 강점
    - 컴포넌트 기반 설계를 통해 재사용성과 유지보수성
    - 상태 관리 및 데이터 흐름을 체계적 관리 가능

- **백엔드**
    - **Django REST Framework (DRF) :** 
    파이썬 기반 Django 웹 프레임워크의 확장으로, RESTful API를 쉽게 개발할 수 있게 해줍니다. 인증, 권한 관리, 데이터 직렬화 기능을 제공합니다.
    - **Django Redis:**
        - **Look Aside(Cache Aside) 패턴**
            - **Cache Warming** : 사용자 데이터(로그인시), 레퍼런스 데이터(1일 1회)
        - **Read Through 패턴**
            - 단체 **POP Quiz**용 퀴즈 캐시에만 저장(1시간)
        - **Write Through 패턴**
            - 사용자 데이터 DB와 캐시에 모두 저장

- **데이터베이스**
    - **PostgreSQL** :
    오픈 소스 관계형 데이터베이스 관리 시스템(RDBMS)으로, 확장성과 고급 쿼리 기능을 제공합니다. Django와도 잘 통합됩니다.
    - **VectorDB** :
    벡터 데이터를 저장하고 검색할 수 있는 데이터베이스입니다. 자연어 처리나 검색 엔진 등에서 사용됩니다.
    - **FAISS** :
    Facebook에서 개발한 벡터 검색 라이브러리로, 빠른 유사도 검색과 클러스터링을 지원합니다.
    - **BM25** :
    텍스트 검색에서 사용하는 순위 모델로, 검색어와 문서 간의 연관성을 측정합니다.

- **LLM**
    - **OpenAI - ChatGPT-4o :**
    OpenAI의 언어 모델 API로, 자연어 처리 및 생성 작업을 백엔드에서 활용할 수 있습니다.
        - **Structured Outputs(4o / 4o-mini)**
            - 사용자가 정의한 구조를 모델 문법으로 사용하는 방식

- **서버 및 클라우드 서비스**
    - **Docker** :
        
        백엔드 및 데이터베이스 서버를 컨테이너화하여 환경 독립성과 이식성을 제공합니다. 이를 통해 애플리케이션을 더 쉽게 배포하고 관리할 수 있습니다.
        
    - **S3, CloudFront, Route 53** :
        
        안정적인 프론트엔드 분리 배포를 지원합니다. S3는 정적 파일을 저장하고, CloudFront는 콘텐츠를 전 세계로 빠르게 배포하며, Route 53은 도메인 이름과 IP 주소를 매핑합니다.
        
    - **도메인 구입, ELB, EC2** :
        
        도메인 구입 및 AWS ELB(Elastic Load Balancer), EC2를 활용해 HTTPS 웹페이지를 활성화하고, 트래픽을 효율적으로 분산시켜 안정성을 보장합니다.

- **협업 도구**
    - **Slack** :
    팀 내 실시간 커뮤니케이션 도구로, 프로젝트 관련 대화, 알림, 파일 공유 등에 사용됩니다.
    - **Figma** :
    클라우드 기반의 UI/UX 디자인 도구로, 실시간 협업 기능을 제공합니다.
    - [**Draw.io](http://Draw.io)** :
    다이어그램 작성 도구로, 프로세스 설계, 데이터 흐름 등을 시각화할 때 사용됩니다.
    - **GitHub** :
    소스 코드 버전 관리 및 협업을 위한 플랫폼으로, 코드 리뷰, 이슈 관리 등을 지원합니다.
    - **Notion** :
    문서 작성, 작업 관리, 데이터 정리를 위한 협업 도구로, 다양한 콘텐츠를 통합적으로 관리할 수 있습니다.
    
# 💭기술적 의사결정

**React** 

- HTML 에 비해 사용자 인터페이스를 구축하고 동적인 웹 애플리케이션 환경을 구축하는데 더 적합하여 채택했습니다.

**Django DRF** 

- AI 기반의 웹서비스에서 Python 언어모델을 사용하는 프레임워크로 Django 를 채택했습니다.
- 프론트엔드와의 분리 구현을 위해 DRF 를 채택했습니다.

- **PostgreSQL**
    - 대규모 데이터를 처리(RAG 관련 전처리데이터, 대화내용 등)하는데 용이합니다.
    - **JSON/JSONB** 등 비정형 데이터와 정형 데이터를 함께 사용할 경우를 고려하여 채택했습니다.

- **Docker**
    - 통일된 개발환경과 실행환경, 최소 2개에서 4개 까지 구성되는 서비스를 통합하여 관리하기 위해 선택했습니다.
    - 배포를 위해 사용할 AWS에서도 Docker 관련한 다양한 기능을 제공하기 때문에 이점이 있을 것이라고 판단했습니다.

- **AWS**
    - **S3** : **React**로 개발된 프론트엔드를 **S3의 정적 웹페이지 호스팅을 이용해 독립적인 배포를 진행했습니다.**
        - S3는 정적 웹 페이지를 호스팅하는 데 매우 저렴한 옵션이며, 사용량 기반 과금이라 초기 비용 부담이 적은 선택이었습니다.또한 트래픽이 증가해도 S3는 자동으로 확장되므로 따로 서버 관리 없이 대응할 수 있게 되었습니다.
    - **CloudFront** : S3로 배포한 프론트엔드 컨텐츠를 전 세계 엣지 로케이션을 활용해 지연 시간을 최소화했으며 정적 컨텐츠를 캐시해 원본 서버의 부하를 감소시켰습니다.
    - **Route53** : 독립적으로 배포된 프론트엔드와 백엔드를 효율적으로 연결하고, 소셜 로그인 기능을 지원하며, 안정적인 웹 페이지 전송을 위한 **HTTPS** 프로토콜을 적용할 수 있도록 구성되었습니다. 이를 위해 도메인 구입이 필수적으로 진행되었으며, 도메인 구입 후 AWS Certificate Manager(ACM)를 이용해 **SSL 인증서**를 발급받아 프론트엔드와 백엔드 간의 보안 연결을 설정할 수 있었습니다.
    - **ELB** : 프론트엔드와 백엔드 간의 외부 데이터 전송 방식을 **HTTPS**로 처리하면서, 내부적으로는 **HTTP**로 전달되도록 포트 포워딩을 수행했습니다. 이를 위해 직접 Nginx를 설정하여 포트 포워딩을 구성할 수도 있었지만, 보다 쉽고 간편한 방법으로 **ELB의 포트 포워딩 기능**을 활용하여 배포된 **EC2 인스턴스의 내부 및 외부 데이터 전송 방식을 효과적으로 조정**했습니다.
    - **EC2** : Django DRF로 개발된 백엔드 서버의 보다 안정적인 환경을 구축하고자 했습니다.
        - **T3** **small** : 여러가지 인스턴스 스펙으로 테스트 해보던 중에 여러명의 사용자가 접속할 경우 동시 다발적인 LLM응답 생성에 대응할 수 있으며 현재 트래픽에서 CPU 크레딧이 여유로운 **T3 small** 모델을 사용했습니다.

- **Docker & AWS**
    - 서비스 미완성 및 불완전을 피하기 위하여 작은 단위의 서비스 구축하며 서비스를 확장해나가는 계획을 수립했습니다.
    - **Docker**와 **AWS**를 같이 활용하면 유지보수 및 확장성의 이점을 가질 수 있다고 판단했습니다.

- **Open AI - GPT-4o**
    - 공식문서 및 다양한 교재를 사용하는 서비스 특성을 고려하여 컨텍스트 용량이 큰 **Open AI**의 모델을 사용했습니다.
    - 일정한 구조의 퀴즈 생성을 위해 **구조화된 출력** 기능을 지원하는 **GPT-4** 이상 모델을 사용했습니다.

# 🔍주요 기능

## 🤖 RAG를 이용한 챗봇 기능
    - 사용자는 원하 카테고리/주제를 선택해 문제를 통한 학습 이전에 간단한 궁금증을 해소하거나 주제 관련 요약을 제공받아 학습 방향을 설정할 수 있습니다.
    - 질문할 수 있는 범위는 AI 강의관련 내용, 강의 관련 오픈소스 코드, 웹 개발 프레임 워크 공식문서입니다.
    - 사용자는 채팅화면 오른쪽에 있는 채팅 세션 파트에서 이전 채팅 내용들을 불러올 수 있습니다.

## 📝 RAG를 이용한 문제 출제/피드백 기능
    - 사용자는 원하는 카테고리/주제/난이도/문제 갯수를 선택해 원하는 주제 내에서 문제를 받아 학습을 진행할 수 있습니다.
    - 출제할 수 있는 범위는 AI 강의관련 내용, 강의 관련 오픈소스 코드, 웹 개발 프레임 워크 공식문서입니다.
    - 문제 풀이 이후에는 사용자의 답변에 대한 피드백을 제공해 사용자의 원할한 학습을 유도합니다.

## 🔐 JWT 인증
    - 백엔드에서 설정할 쿠키에는 짧은 생명 주기의 AccessToken만 저장합니다.
    - 해당 AccessToken을 갱신할 때에는 accessToken을 디코딩하여 사용자를 인식한 후 사용자에 맞는 refreshToken을 DB에서 가져옵니다.
    - refreshToken 만료 기한 이전에 자동으로 accessToken을 자동 갱신하게 하기 위해 로그인할 때 발급되는 시점에서 프론트 측에서 로그인 시간을 기록해 둔 후 자동으로 백엔드 측에서 설정해둔 accessToken 만료 기한 이전에 refreshToken 갱신 API를 호출한 후 새로 발급된 accessToken을 프론트 측에 저장해 둬 로그인을 유지할 수 있게 됩니다.

## 🌐 소셜 로그인
    - OAuth를 통해 구글 로그인 페이지로 연결합니다.
    - 구글 로그인 통해 빠르게 회원등록 및 로그인 할 수 있습니다.
    - 이메일 주소 앞부분을 제외한 다른 정보를 사용하지 않습니다.
    
## 💬 Polling 방식을 활용한 실시간 채팅
    - 실시간으로 대화가 저장/관리가 가능합니다.
    - 각 채팅은 주지/카테고리 별로 선택할 수 있습니다.
    - 새로운 채팅방 생성 시/채팅방 선택 시에 해당 채팅방 위치로 자동 스크롤을 가능하게 합니다.
    - 코드와 일반 Text를 구분해 사용자에게 좋은 채팅 뷰를 제공하고자 합니다.

## 🍿 Websocket 방식을 활용한 단체 참여 POP QUIZ
    - redis 서버를 활용하여 각 클라이언트와 서버간의 웹소켓 방식을 구현했습니다.
    - 정해진 시간마다 채팅창에 POP QUIZ가 생성되면, 유저들은 화면을 보고 퀴즈를 풀게됩니다.
    - 문제를 먼저 맞춘 유저는 RiddleScore를 획득하고, 왼쪽 랭킹판에 점수가 갱신됩니다.
    - 제한시간 내에 참여자들이 모두 문제를 맞추지 못한 경우, ReadRiddle이 정답을 공개하고 다음 QUIZ까지 대기시간이 적용됩니다.
    