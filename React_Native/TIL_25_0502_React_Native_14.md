# To-Do 앱 로직 요약

## 입력 이벤트 처리
- 사용자가 텍스트 입력 후 제출할 때를 감지하기 위해 `onSubmitEditing` 이벤트 사용
- 해당 이벤트에서 `addToDo` 함수 호출
- `addToDo` 함수는 현재 입력된 텍스트(alert)로 확인

## 키보드 설정
- 리턴 키를 `"done"`으로 설정하여 UX 향상

## 입력 유효성 검사 및 초기화
- 입력값이 비어 있으면 아무 동작도 하지 않음 (`return`)
- 유효한 입력일 경우 나중에 저장할 로직은 생략하고, 입력 필드 초기화 (`setText("")`)

## to-do 상태(state) 구조 정의
- `useState`를 사용하여 `todos` 상태를 객체(object)로 정의
- 객체의 키는 `Date.now()`를 이용한 고유 ID
- 각 to-do 항목은 `{ text: '내용', work: true/false }` 형태

## React 상태 관리 규칙
- React에서는 상태를 직접 변경하면 안 됨 (예: `todos[id] = value`는 불가)
- 항상 새 객체를 생성하여 상태 업데이트 해야 함

## `Object.assign` 사용
- 기존 todos 객체와 새 to-do 항목을 병합한 새 객체 생성
- 형식: `Object.assign({}, 기존객체, 새로운객체)`
- 동적으로 키를 만들 때는 `[]` 문법 사용 (예: `[Date.now()]: { text, work }`)

## 최종 동작 확인
- to-do 항목을 추가한 뒤 `console.log(todos)`로 상태 확인
- 입력된 여러 to-do 항목들이 ID 기반으로 잘 저장되는지 확인

## 다음 단계 예고
- 다음 영상에서는 저장된 to-do 항목들을 화면에 출력하기 위해 ScrollView 구성 예정
