## React Native Touchable 컴포넌트 정리

- **헤더 구성 시작**  
  - 앱 상단에 `Work`, `Travel` 버튼을 배치  
  - 버튼 클릭 시 아래 내용이 변경되도록 구성  

- **스타일링 기본 설정**  
  - `flexDirection: 'row'`로 버튼을 가로 배치  
  - `fontSize`, `fontWeight` 등으로 텍스트 크기 및 굵기 조정  
  - `paddingHorizontal`, `marginTop` 등으로 여백 설정  

- **테마 색상 관리**  
  - `colors.js` 파일 생성하여 색상 테마 객체로 관리  
  - 선택된 버튼은 흰색, 비활성 버튼은 회색으로 표현  

- **TouchableOpacity**  
  - 기본적인 터치 이벤트 처리용 컴포넌트  
  - 터치 시 불투명도(opacity)가 변해 시각적 피드백 제공  
  - `onPress` 이벤트로 동작 처리 가능  

- **TouchableHighlight**  
  - 터치 시 배경 색상이 변경되는 컴포넌트  
  - `underlayColor` 속성으로 터치 시 나타날 배경 색 지정  
  - `onPress`, `onPressIn`, `onPressOut` 등 다양한 이벤트 사용 가능  

- **TouchableWithoutFeedback**  
  - 시각적 피드백 없이 터치 이벤트만 감지  
  - UI 변화 없이 동작만 처리하고자 할 때 사용  
  - `onPress` 등 이벤트는 동일하게 사용 가능  

- **Pressable (신규 컴포넌트)**  
  - 더 많은 설정이 가능한 터치 처리 컴포넌트  
  - `onPress`, `onPressIn`, `onPressOut`, `onLongPress` 등 지원  
  - `delayLongPress`, `disabled`, `hitSlop` 등 고급 속성 제공  

- **hitSlop 설명**  
  - 터치 감지 영역을 시각적 요소보다 크게 설정 가능  
  - 작은 요소라도 주변을 넓게 감지시켜 UX 향상  

- **실제 사용**  
  - 간단한 인터페이스에는 `TouchableOpacity`를 주로 사용  
  - 배경 색 변화가 필요할 경우 `TouchableHighlight`  
  - UI 피드백이 필요 없는 경우 `TouchableWithoutFeedback`  
  - 고급 제어가 필요할 경우 `Pressable` 사용  
