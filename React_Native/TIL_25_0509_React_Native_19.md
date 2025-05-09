# React Native + Expo: 멀티 플랫폼

## 앱 업데이트 및 Expo 사용
- Expo를 통해 앱을 간편하게 업데이트할 수 있음
- `expo publish` 또는 Expo GUI에서 "Publish" 클릭으로 배포 가능

## 앱 초기화 화면(Splash Screen) 및 아이콘 변경
- `app.json` 파일에서 설정
- 설정 예시:
```json
{
  "expo": {
    "name": "MyApp",
    "splash": {
      "image": "./assets/splash.png",
      "backgroundColor": "#ffffff"
    },
    "icon": "./assets/icon.png"
  }
}
```

## 플랫폼별 코드 분기 처리
- `Platform.OS`를 사용하여 플랫폼 감지
- 예시:
```js
import { Platform, Alert } from 'react-native';

if (Platform.OS === 'web') {
  if (confirm('삭제하시겠습니까?')) {
    // 웹용 삭제 처리
  }
} else {
  Alert.alert('삭제하시겠습니까?');
}
```

## 웹에서 `Alert` 사용 불가
- `alert()` 및 `confirm()`은 브라우저용 API
- React Native의 `Alert`는 iOS, Android에서만 작동

## 플랫폼 지원 범위
- React Native는 iOS, Android 외에도 Web, Windows, macOS, VR 지원
- 플랫폼 구분 키:
```js
Platform.OS === 'ios' | 'android' | 'web' | 'windows' | 'macos'
```

## 스타일 버그 해결
- 외부 스타일시트를 직접 컴포넌트에 인라인 적용하면 일부 스타일 문제 해결 가능
- 예:
```js
<Text style={{ fontSize: 20 }}>버튼 텍스트</Text>
```

## 앱 설정 파일(app.json)의 역할
- 앱 이름, 로고, 지원 플랫폼, 소셜 로그인, 다국어 등 설정 가능
- iOS/Android 각각의 속성을 별도로 지정 가능

## 멀티 플랫폼 개발 환경 구성
- Android/iOS 시뮬레이터로 테스트 가능
- 웹은 Expo Web을 통해 바로 확인 가능