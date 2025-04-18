# React Native 패키지 및 컴포넌트 구조 변화 정리

## 핵심 개념 요약

- **React Native 문서 사이트**에서는 핵심 컴포넌트(core components)와 API를 확인할 수 있음.
- 핵심 컴포넌트 예시: `Text`, `View`, `Button`, `Image`, `StatusBar` 등.
- 일부 컴포넌트는 **Android 전용** 또는 **iOS 전용**으로 제공됨.


## 예전과 달라진 점

- 과거에는 `AsyncStorage`, `NavigatorIOS`, `DatePickerIOS`, `ToolbarAndroid` 등 다양한 컴포넌트가 포함되어 있었음.
- 현재는 이런 컴포넌트 대부분이 **삭제**되었거나 **커뮤니티 패키지**로 분리됨.


## 변경 이유

- 플랫폼 전용 컴포넌트(iOS/Android)가 많아지면서 **유지보수와 버그 관리가 어려워짐**.
- React Native 팀은 더 이상 모든 기능을 직접 지원하지 않기로 결정함.
- 필수적인 컴포넌트만 React Native에 포함시키고, 나머지는 **외부 패키지**에 위임.


## 대표적인 변화 예시

- `AsyncStorage`  
  - 과거: React Native에서 기본 제공  
  - 현재: **`@react-native-async-storage/async-storage`** 와 같은 커뮤니티 패키지 사용 권장

- **탭 네비게이션, 스크린 전환** 등의 네비게이션 기능은 직접 제공되지 않음 → `react-navigation`과 같은 외부 라이브러리 사용 필요


## 요약

- React Native는 과거에 많은 컴포넌트와 API를 지원했지만, 현재는 **가볍고 핵심 기능 중심**으로 바뀜.
- 개발자는 필요한 기능을 커뮤니티 패키지에서 가져와야 하며, 공식 문서에서는 필수적인 컴포넌트만 제공함.

