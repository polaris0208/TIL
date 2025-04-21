# React Native Packages

## 기본 개념
- React Native 공식 문서에서 **Core Components** (텍스트, 뷰 등)를 제공
- 슬로건: "Learn once, write anywhere"

## Core Components
- 제공되는 컴포넌트 수는 적음 (예: `Text`, `View`, `Image`, `Button`)
- 일부는 플랫폼 전용 (Android 전용 / iOS 전용)

## 과거에는 더 많은 컴포넌트 제공
- 예전에는 `AsyncStorage`, `NavigatorIOS`, `DatePickerIOS` 등 다양한 컴포넌트 존재
- 현재는 대부분 제거됨

## 제거된 기능 예시
- `AsyncStorage`: 과거에는 내장되어 있었으나 현재는 **사용 중단(deprecated)** → **커뮤니티 패키지 사용 권장**
- `NavigatorIOS`, `DatePickerIOS`, `TabBarIOS` 등도 사라짐

## 이유: 유지보수의 어려움
- 초기에 너무 많은 기능과 API를 지원하려 했음
- 플랫폼별 컴포넌트가 많아지며 코드가 복잡해짐
- 버그 증가, 업데이트 어려움 등 문제 발생

## 전략 변경
- React Native 팀은 **최소한의 핵심 컴포넌트만 유지**하는 방향으로 전환
- 성능 개선과 유지보수 용이성을 목표로 함
- 부가 기능은 **커뮤니티 패키지**에 위임 (예: `@react-native-async-storage/async-storage`)

## 현재 방향성 요약
- React Native는 필수 요소만 자체 지원
- 그 외 기능은 커뮤니티 패키지를 통해 확장
- 목적: 속도와 안정성 강화
