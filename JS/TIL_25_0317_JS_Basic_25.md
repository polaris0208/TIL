# To-Do 리스트 삭제 2

## 개념

- To-Do 항목 삭제는 특정 ID를 가진 항목을 제외하는 방식으로 동작함.
- `filter()` 함수는 기존 배열을 변경하지 않고 새로운 배열을 반환함.
- 삭제 후에는 업데이트된 To-Do 목록을 로컬 스토리지에 저장해야 함.

## 주요 개념 정리

- `filter()` 함수는 기존 배열을 변경하지 않음.
- `filter()`를 사용하여 특정 ID를 제외한 새로운 배열 생성.
- `parseInt()`를 사용하여 문자열 ID를 숫자로 변환해야 타입 오류 방지 가능.
- 삭제 후 `saveToDos()`를 호출하여 변경 사항을 저장해야 함.

## 예시

```javascript
// 기존 To-Do 리스트
let todos = [
    { id: 1, text: "할 일 1" },
    { id: 2, text: "할 일 2" },
    { id: 3, text: "할 일 3" }
];

// 특정 ID를 가진 To-Do 삭제 함수
function deleteTodo(clickedId) {
    // ID를 숫자로 변환
    const idToRemove = parseInt(clickedId);
    
    // 해당 ID를 제외한 새로운 배열 생성
    todos = todos.filter(todo => todo.id !== idToRemove);
    
    // 변경된 목록 저장
    saveToDos();
}

// 변경된 To-Do 리스트 저장 함수 (예제)
function saveToDos() {
    localStorage.setItem("todos", JSON.stringify(todos));
}

// 테스트 실행
console.log("삭제 전:", todos);
deleteTodo("2"); // ID 2 삭제
console.log("삭제 후:", todos);
```

## 실행 흐름

1. `deleteTodo("2")` 호출 → `clickedId` 값이 문자열 "2".
2. `parseInt(clickedId)`를 통해 숫자 `2`로 변환.
3. `filter()`를 사용하여 ID가 2가 아닌 항목만 남긴 새로운 배열 생성.
4. 변경된 To-Do 리스트를 `localStorage`에 저장.
5. 결과적으로 ID가 2인 항목이 제거된 상태 유지.

