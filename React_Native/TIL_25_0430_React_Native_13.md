# TextInput 개념 정리

- React.js에서는 상태(state)로 `working`을 관리하며, `travel()`과 `work()` 함수를 통해 상태 전환을 구현함  
- 텍스트를 클릭했을 때 해당 함수가 호출되어 상태 변경 및 스타일 변경이 가능함  
- 스타일은 객체 형태로 적용되며, 기존 스타일에 덧붙이기 위해 전개 연산자(`...`)를 사용함  
- 조건에 따라 색상(`white`, `gray`)을 다르게 지정하여 시각적으로 상태 구분 가능함


- React Native에서는 `TextInput` 컴포넌트를 통해 텍스트 입력을 처리함  
- `TextInput`은 HTML의 `textarea` 없이 단일 컴포넌트로 입력 기능을 담당함  
- `placeholder`를 상태에 따라 다르게 설정 가능함 (예: 작업 중일 때, 여행 중일 때)


- 스타일 속성으로 `paddingVertical`, `paddingHorizontal`, `borderRadius`, `marginTop`, `fontSize` 등을 설정하여 입력창 디자인 가능  
- `keyboardType`을 통해 숫자, 이메일, 전화번호 등 입력 유형에 맞는 키보드 제공 가능함  
  - 예시: `"number-pad"`, `"email-address"`, `"phone-pad"`, `"url"` 등


- `returnKeyType`을 사용하면 키보드의 반환 키에 표시되는 텍스트 변경 가능  
  - 예시: `"send"`, `"search"`, `"next"`, `"done"` 등


- `secureTextEntry` 속성으로 비밀번호 입력처럼 텍스트를 숨김 처리할 수 있음  
- `multiline` 속성을 사용하면 여러 줄 입력이 가능함


- `placeholderTextColor`로 플레이스홀더 텍스트의 색상도 지정 가능  
- `onChangeText`를 통해 입력된 값을 실시간으로 상태에 반영 가능  
  - 예시: `onChangeText={(text) => setText(text)}`


- 추가 속성으로는 `autoCorrect`, `autoCapitalize` 등이 있으며, 자동 수정 및 대문자 변환 제어 가능  
- 최종적으로 `TextInput`에 `value`와 `onChangeText`를 설정해 **컨트롤드 컴포넌트**로 관리함
