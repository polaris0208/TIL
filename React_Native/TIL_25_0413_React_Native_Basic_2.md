# React Native 앱 생성

## Expo CLI와 Expo Go 설치

- **Expo CLI**: React Native 프로젝트를 쉽게 시작하고 관리할 수 있는 CLI 도구  
- **Expo Go**: 실제 스마트폰에서 앱을 실행할 수 있는 앱

```bash
npm install -g expo-cli
```

스마트폰에 **Expo Go** 앱 설치 (iOS App Store / Android Play Store)

## 프로젝트 생성

- `expo init` 명령어로 새 프로젝트 생성
- 템플릿 중 **blank (JavaScript)** 선택

```bash
expo init nomadweather
```

## 폴더 구조 확인

생성된 폴더 구조:

- `App.js`: 메인 앱 로직 파일
- `assets/`: 이미지 등 리소스 저장 폴더
- `package.json`: 프로젝트 설정 및 의존성 관리 파일

> `App.js`가 실제 앱 UI의 시작점

## 앱 실행 준비

- 시뮬레이터 없이 **스마트폰으로 실행**
- 다음 명령어로 앱 실행:

```bash
npm start
```

- 실행 후 브라우저에 QR 코드가 뜸
- 스마트폰 Expo Go 앱으로 QR 코드 스캔

## 로그인 설정 (동기화 목적)

- **Expo 계정**으로 로그인 필요 (PC와 스마트폰 모두)

```bash
expo login
```

- 로그인 후 다시 앱 실행:

```bash
npm start
```

## 코드 수정 및 실시간 반영

`App.js`를 열어 텍스트 수정 후 저장하면, **스마트폰 앱에서 바로 반영**

```jsx
// App.js 예시
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View>
      <Text>Hello, I made a React Native app!</Text>
    </View>
  );
}
```

## 핵심 개념 요약

- Expo를 사용하면 시뮬레이터 없이도 **간편하게 앱 실행** 가능
- 코드 수정 시 **실시간으로 스마트폰에 반영**
- `npm start` 후 QR 코드로 바로 앱 확인 가능
- `App.js`에서 앱 로직 시작