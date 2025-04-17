# React Native 기본 규칙 정리

## 뷰 컴포넌트 (View)

- React Native에서는 HTML의 `div` 대신 `View`를 사용함.
- `View`는 컨테이너 역할을 하며 박스처럼 작동함.
- 항상 `View`를 사용하려면 import가 필요함.

```js
import { View } from 'react-native';

export default function App() {
  return <View></View>;
}
```

## 텍스트 컴포넌트 (Text)

- 모든 텍스트는 반드시 `Text` 컴포넌트 안에 있어야 함.
- `span`, `p`, `h1` 같은 HTML 태그는 존재하지 않음.
- 텍스트를 `View`에 직접 넣으면 오류 발생.

```js
import { Text, View } from 'react-native';

export default function App() {
  return (
    <View>
      <Text>Hello React Native!</Text>
    </View>
  );
}
```

## 스타일 작성 방법

- 스타일은 JavaScript 객체로 작성함.
- `StyleSheet.create()`를 사용하면 자동완성 기능을 활용 가능.
- 직접 객체로 넣어도 되지만, 파일이 길어질 수 있음.

```js
import { StyleSheet, Text, View } from 'react-native';

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'lightblue',
    padding: 20,
  },
  text: {
    fontSize: 24,
    color: 'white',
  },
});

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Styled Text</Text>
    </View>
  );
}
```

- `StyleSheet.create()`를 사용하지 않고 직접 객체로 작성도 가능:

```js
export default function App() {
  return (
    <View style={{ backgroundColor: 'lightblue', padding: 20 }}>
      <Text style={{ fontSize: 24, color: 'white' }}>Inline Styled Text</Text>
    </View>
  );
}
```

## CSS와의 차이점

- React Native에서는 모든 스타일을 camelCase로 작성함 (예: `fontSize`, `backgroundColor`).
- 웹에서 사용하는 `border: 1px dashed green` 같은 속성은 사용할 수 없음.
- 지원하는 스타일 속성만 사용 가능. 오류 시 친절한 에러 메시지를 제공함.

## StatusBar 컴포넌트

- `StatusBar`는 화면에 보이지 않지만 운영체제의 상단 상태 표시줄(iOS/Android)을 설정하는 컴포넌트임.
- `react-native`에서 기본 제공하지 않으며, 보통 `expo-status-bar` 패키지를 통해 사용됨.

```js
import { StatusBar } from 'expo-status-bar';

export default function App() {
  return (
    <>
      <StatusBar style="light" />
      <View style={{ flex: 1, backgroundColor: 'black' }}>
        <Text style={{ color: 'white' }}>Hello!</Text>
      </View>
    </>
  );
}
```

## 요약

- `div` → `View`, `span` → `Text`
- 텍스트는 항상 `Text` 안에 작성
- 스타일은 객체 형식, `StyleSheet.create()` 사용 권장
- CSS와 다르게 일부 속성만 사용 가능
- `StatusBar`는 화면이 아닌 운영체제와 상호작용하는 특수 컴포넌트