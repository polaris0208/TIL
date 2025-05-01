# Rider를 활용한 C# 프로그래밍 환경 설정

## JetBrains Rider 설치

- [Rider 다운로드 페이지](https://www.jetbrains.com/rider/download)에서 설치 파일(.exe, .dmg, .tar.gz 등) 다운로드 및 설치
- JetBrains Toolbox App 사용 시 여러 JetBrains 제품 통합 관리 가능
- 설치 후 JetBrains 계정 로그인  
  - 학생 인증 시 1년 무료 라이선스 발급 가능 (JetBrains 공식 정책)
- 설치 옵션에서 다음 항목 선택 가능:
  - 바탕화면 바로가기
  - PATH 등록
  - 파일 연결 등

## .NET SDK 설치

- [Microsoft 공식 사이트](https://dotnet.microsoft.com/)에서 최신 .NET SDK 다운로드 및 설치
- Rider는 설치된 SDK를 자동 인식  
  - 인식하지 못할 경우: Rider 환경설정에서 SDK 경로 수동 지정 가능

## Rider 첫 실행 및 초기 설정

- 첫 실행 시 테마, 키맵 등 개인 취향에 맞게 설정
- 플러그인 설치 가능 (예: Unity, Git 등)
  - Unity Support 플러그인 기본 내장 → 필요 시 활성화
  - 기타 플러그인은 `Settings → Plugins`에서 설치 가능

## 새 C# 콘솔 프로젝트 생성

1. Rider 실행 후 "New Solution" 클릭 → "Console Application" 선택
2. 프로젝트명, 저장 경로 지정 후 생성
3. 생성된 기본 `Program.cs` 파일에서 코드 작성 가능

## 프로젝트 빌드 및 실행

- 상단 Run 버튼 클릭 또는 `Shift + F10` (Windows 기준) 실행
- 하단 터미널에서 결과 확인 (예: `Hello, World!` 출력)

## Unity 등 게임 엔진 연동

- Unity에서 Rider 연동:
  - `Edit → Preferences → External Tools → External Script Editor` → Rider 선택
- Unity 프로젝트에서 C# 스크립트 더블 클릭 시 Rider 자동 연결
- Rider 지원 기능:
  - Unity 전용 코드 자동완성
  - 이벤트 함수 자동 생성
- 필수 설정:
  - Unity Support 플러그인 활성화
  - Unity Editor 패키지 설치

## Rider 주요 기능

- 코드 자동완성, 실시간 코드 분석, 리팩토링
- Git 등 버전 관리 도구 통합
- 다양한 단축키, 라이브 템플릿 제공으로 생산성 향상

## 문제 상황 및 해결

- SDK 미인식 시:
  - SDK 재설치 또는 Rider 재시작
- Unity 연동 문제 시:
  - Unity에서 외부 에디터 설정 확인
  - Rider Editor 패키지 설치 여부 확인
