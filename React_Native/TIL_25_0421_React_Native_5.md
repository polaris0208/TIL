# React Native와 서드파티 패키지 개념 정리

## React Native의 변화
- 과거에는 다양한 컴포넌트와 API를 공식적으로 제공했음
- 현재는 **핵심 기능만 유지**하고, 나머지는 커뮤니티에 맡김
- 이유: 더 빠르게, 더 가볍게, 더 유지보수하기 쉽게 만들기 위해

## 컴포넌트와 API의 차이
- **컴포넌트**: 화면에 렌더링되는 요소 (예: `<View>`, `<StatusBar>`)
- **API**: 자바스크립트 코드로 기능을 제공함 (예: `Vibration.vibrate()`)

## 커뮤니티 패키지의 필요성
- 공식 지원이 줄어들면서 **서드파티 패키지를 활용**해야 함
- 예: `AsyncStorage`는 더 이상 React Native에서 제공하지 않음 → 커뮤니티 패키지 사용 필요

## React Native Directory
- 다양한 커뮤니티 패키지를 소개하는 웹사이트
- 각 패키지의 **업데이트 주기, 다운로드 수 등**을 보고 신뢰도 확인 가능

## Expo의 역할
- Expo는 **중요한 기능들**을 자체적으로 패키지화하여 지원
- `expo install` 명령어로 쉽게 설치 가능
- **대표적인 Expo API 예시**:
  - Document Picker
  - SMS 발송
  - StatusBar (React Native 버전보다 향상된 버전)
  - Async Storage (권장 커뮤니티 버전 지원)
  - Local Authentication (지문 등)
  - Map View 등

## Expo vs React Native
- 동일한 기능을 갖는 컴포넌트라도 **Expo가 기능을 확장하거나 사용성을 개선**한 버전 제공
- Expo의 장점:
  - 안정적이고 버그가 적음
  - 필요한 대부분의 패키지를 포함
  - 설치 및 사용이 간편함
  - 훌륭한 문서화

## 결론
- React Native는 핵심 기능만 제공하고, **나머지는 커뮤니티나 Expo를 통해 확장**해야 함
- Expo는 필수 기능을 잘 정리해놓은 훌륭한 도구로, 앱 개발을 훨씬 쉽게 만들어줌
