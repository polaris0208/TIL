### React Native의 작동 원리

- **React Native는 웹뷰나 브라우저 기반이 아니다**
  - 일반 웹사이트처럼 HTML과 CSS를 만들어서 브라우저에 보여주는 구조가 아님
  - 내부에 웹 브라우저가 포함된 앱이 아님

- **React Native는 자바스크립트 ↔ 네이티브 간의 '통역사' 역할을 한다**
  - React Native는 우리가 작성한 JavaScript 코드를 iOS (Swift/Objective-C), Android (Java/Kotlin) 코드로 변환하여 네이티브 UI를 생성
  - 따라서 iOS에서는 iOS 스타일 버튼, Android에서는 Android 스타일 버튼이 보여짐

- **브라우저 대신 'Bridge(브릿지)'를 통해 통신함**
  - JavaScript와 네이티브 간에 메시지를 주고받는 통로가 브릿지
  - 이 브릿지를 통해 이벤트, UI 요청 등이 전달됨

- **앱의 구성 요소**
  - JavaScript 코드 (우리가 작성)
  - React Native (Bridge 역할)
  - Native 코드 (iOS/Android에서 실제 UI 처리)

- **이벤트 처리 흐름**
  1. 유저가 화면을 터치
  2. iOS/Android가 터치 이벤트 감지
  3. 이벤트 정보를 브릿지를 통해 JavaScript로 전달
  4. JavaScript에서 로직 처리 (예: 색상 변경)
  5. 다시 브릿지를 통해 네이티브 측에 UI 변경 요청

- **개발자가 직접 작성하는 코드는 대부분 JavaScript**
  - 스타일과 로직을 포함한 컴포넌트 코드만 작성
  - 나머지 네이티브 연결, 브릿지 처리 등은 React Native가 자동 처리

### 코드 예시

```jsx
import React from 'react';
import { View, Button, StyleSheet } from 'react-native';

const App = () => {
  const changeColor = () => {
    console.log('버튼 클릭됨 → 배경색을 변경 요청');
    // 실제로는 상태(state)를 이용해 배경색을 변경할 수 있음
  };

  return (
    <View style={styles.container}>
      <Button title="배경색 변경" onPress={changeColor} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    justifyContent: 'center',
    padding: 16,
  },
});

export default App;
```

### 요약

- React Native는 웹이 아닌 **진짜 네이티브 앱을 만드는 도구**
- JavaScript만 작성하면, React Native가 이를 **브릿지를 통해** iOS/Android에 전달
- 이벤트 감지, UI 렌더링은 모두 iOS/Android가 처리
- 개발자는 **JavaScript 코드에 집중**하면 됨