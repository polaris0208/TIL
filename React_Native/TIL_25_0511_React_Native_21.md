# Expo로 앱 개발: 장점과 한계

## Expo의 장점

- **간편한 앱 빌드**
  - `expo build:android`, `expo build:ios` 명령어로 쉽게 빌드 가능
  - 별도 환경설정 없이 실행 가능

- **풍부한 SDK 제공**
  - 기본적으로 많은 기능 내장  
    (예: `SMS`, `SQLite`, `Stripe`, `In-App Purchases`, `Google Login`, `Face Detection` 등)

- **편리한 개발 환경 제공**
  - QR 코드로 앱 실행
  - 웹에서 실시간 프리뷰 가능
  - 다양한 디바이스 연결 쉽게 확인 가능

- **JavaScript 중심 개발**
  - `app.json`과 JavaScript 파일만으로 대부분의 앱 구현 가능

```bash
expo install expo-sqlite
expo install expo-media-library
```


## Expo의 한계

- **Native 코드에 접근 불가**
  - `AndroidManifest.xml`, `build.gradle`, `Info.plist` 등 네이티브 설정 파일 수정 불가

- **외부 라이브러리 통합 제한**
  - 예: `react-native-ble-plx` (블루투스 저에너지 통신용) 같은 네이티브 연동 라이브러리 사용 불가

```bash
# 사용 불가 예시 (Expo에서는 안 됨)
npm install --save react-native-ble-plx
cd ios && pod install  # iOS 네이티브 설정 필요
```

- **앱 용량이 큼**
  - 불필요한 SDK 포함됨 (예: Facebook SDK 기본 포함)
  - 간단한 앱도 60MB 이상 될 수 있음

- **유연한 설정 부족**
  - 앱 사이즈 최적화, 고급 기능 추가 불가


## 해결 방법

### 1. `expo eject` 명령어

- Expo에서 벗어나 React Native 환경으로 전환
- 네이티브 설정 파일들에 접근 가능

```bash
npx expo eject
```

> eject 후에는 더 이상 Expo 관리 하에 있지 않으며, 네이티브 환경 설정 책임이 생김

### 2. Create React Native App 사용 권장

- Expo SDK 사용 가능
- 동시에 네이티브 설정 접근 가능

```bash
npx create-react-native-app myApp
```
