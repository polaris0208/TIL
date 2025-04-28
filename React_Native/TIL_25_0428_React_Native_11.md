# Expo Vector Icons 사용법 정리

## 디자인 변경
- 숫자 크기 축소, 전체 왼쪽 정렬, 색상 흰색으로 변경

## Expo Vector Icons 소개
- `expo init`으로 생성한 프로젝트에는 **Expo Vector Icons** 패키지가 기본 설치되어 있음
- 다양한 아이콘을 쉽게 사용할 수 있음

## 아이콘 사용 방법
- 사용할 **아이콘 패밀리**를 import
- 아이콘 이름을 지정해 컴포넌트로 사용
- 참고 사이트: [https://icons.expo.fyi/](https://icons.expo.fyi/)

## 아이콘 패밀리 종류
- 예시
  - FontAwesome
  - EvilIcons
  - Fontisto
- 패밀리에 따라 아이콘 스타일이 다름
- 프로젝트에 맞는 스타일 선택

## 날씨 아이콘 매핑
- 날씨 API의 조건(Main)을 기준으로 아이콘 매칭
- 예시
  - `clear` → `day-sunny`
  - `clouds` → `cloudy`
  - `snow` → `snow`
  - `rain` → `rain`
  - `thunderstorm` → `lightning`
  - `drizzle` → `tiny rain` 대체 사용
  - `atmosphere` → 적당한 아이콘 선택 (예: `cloudy-gusts`)

## 구현 방법
- 날씨 조건을 키(key), 아이콘 이름을 값(value)으로 가지는 **객체** 생성
- 예시 코드
  ```javascript
  const icons = {
    Clear: "day-sunny",
    Clouds: "cloudy",
    Snow: "snow",
    Rain: "rain",
    Thunderstorm: "lightning",
    Drizzle: "rain",
    Atmosphere: "cloudy-gusts",
  };
  ```
- 실제 표시할 때는 날씨 데이터의 `main` 값을 기준으로 icons 객체에서 아이콘 이름을 찾아 사용

## 레이아웃 조정
- 아이콘과 온도를 같은 View에 묶고, `flexDirection: "row"`, `alignItems: "center"`로 정렬
- 아이콘 크기와 간격 조정하여 보기 좋게 배치

## 스타일 결합 방법
- 여러 스타일을 하나로 합치기
- 예시
  ```javascript
  style={[styles.default, { marginTop: 10 }]}
  ```
- React Native가 아닌 일반 JavaScript(ES6) 문법

## 최종 결과
- 다양한 날씨 조건에 맞게 아이콘 정상 표시 완료
- 다음 단계: **투두 리스트(To-Do List) 앱** 개발로 넘어감