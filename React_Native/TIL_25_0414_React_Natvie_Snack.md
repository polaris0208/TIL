### Snack 개념 정리

- **Snack이란?**  
  Expo에서 제공하는 온라인 React Native 개발 도구로, 브라우저만으로 앱을 개발하고 실행할 수 있음.

- **설치 불필요**  
  Node.js, Visual Studio Code, 안드로이드/iOS 시뮬레이터 없이 개발 가능.

- **브라우저 기반 시뮬레이터 제공**  
  - iOS, Android, Web 미리보기 지원  
  - 실시간 코드 반영 및 결과 확인 가능

- **QR 코드로 실기기 미리보기 가능**  
  Expo 앱이 설치된 스마트폰에서 QR 코드를 스캔하면 바로 앱 실행 가능.

- **Expo 계정 연동 기능**  
  로그인하면 QR 코드 없이도 스마트폰에서 자동으로 앱 확인 가능.

- **프로젝트 저장 및 공유**  
  코드를 저장하면 고유 URL 생성 → 다른 사람과 공유 및 디버깅 가능.

- **문제 해결 및 피드백**  
  문제가 생기면 코드 복사해서 Snack에 붙여넣고 링크 공유하면 도움 요청 용이.

---

### 기본 사용 예시

```jsx
import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Hello, Snack!</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});
```

- 위 코드를 [https://snack.expo.dev](https://snack.expo.dev)에 붙여넣으면 바로 실행 가능
- 저장 후 생성된 URL로 누구나 동일한 앱을 확인 가능