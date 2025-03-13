# To-Do 목록 불러오기

## 개념 정리

- **로컬 스토리지 활용**
  - 브라우저의 `localStorage`를 사용하여 데이터를 저장 및 불러올 수 있음
  - 새로고침 후에도 데이터 유지 가능

- **JSON 데이터 변환**
  - `JSON.stringify(배열)` → 배열을 문자열로 변환하여 저장
  - `JSON.parse(문자열)` → 문자열을 다시 배열로 변환하여 사용

- **데이터 가져오기 및 변환**
  - `localStorage.getItem("todos")`으로 저장된 문자열을 가져옴
  - `JSON.parse()`를 사용하여 배열로 변환
  - 데이터가 없을 경우 `null`이 반환되므로 예외 처리 필요

- **배열 순회 및 출력**
  - `forEach()`를 사용하여 배열의 각 항목을 처리 가능
  - 각 항목을 화면에 표시하거나 조작할 수 있음

- **화살표 함수 활용**
  - 기존 함수 선언 방식 대신 간결한 화살표 함수 사용 가능

## 코드 예시

```javascript
// 로컬 스토리지에서 To-Do 목록 불러오기
const savedTodos = localStorage.getItem("todos");
let parsedTodos = [];

// 저장된 값이 있을 경우 JSON 변환
if (savedTodos !== null) {
    parsedTodos = JSON.parse(savedTodos);
}

// 배열 순회 및 출력
parsedTodos.forEach(todo => {
    console.log(`현재 처리 중인 항목: ${todo}`);
});

// 화살표 함수 사용 예시
parsedTodos.forEach(todo => console.log(`처리 중: ${todo}`));
```

## 추가 설명

- `localStorage.setItem("todos", JSON.stringify(배열))`을 사용하여 데이터를 저장 가능
- 데이터가 없는 경우 대비하여 `null` 체크 후 처리하는 것이 중요함
- `forEach()`를 활용하면 각 항목을 순차적으로 처리할 수 있음
- 화살표 함수(`=>`)를 사용하면 코드가 더 간결해짐