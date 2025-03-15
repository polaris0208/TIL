# To-Do 리스트 삭제

## 문제점
- 할 일을 삭제해도 **로컬 스토리지(Local Storage)** 가 업데이트되지 않음
- 로컬 스토리지를 데이터베이스처럼 생각하면 안 됨
  - 실제 데이터베이스는 **배열(Array)**
  - 로컬 스토리지는 단순히 배열을 저장하는 공간

## 해결책: 할 일에 고유 ID 부여하기
- 동일한 텍스트의 할 일이 여러 개 있을 경우 어떤 항목을 삭제해야 할지 구분 불가능
- 각 할 일마다 **고유 ID**를 추가해 구별하도록 개선

## ID 생성 방법
- `Date.now()`를 사용하여 고유한 숫자 ID 생성

```javascript
const newTodo = {
  id: Date.now(),
  text: newTodoValue
};
```

## ID가 포함된 할 일 저장 방식 변경
- 기존 방식: 문자열만 저장
- 변경 후: 객체(Object)로 저장

```javascript
// 기존 방식
const todos = [];
todos.push("할 일 1");

// 변경 후
const todos = [];
todos.push({ id: Date.now(), text: "할 일 1" });
```

## HTML 요소에 ID 적용
- 각 `li` 요소에 ID를 추가하여 특정 할 일을 식별 가능하도록 변경

```javascript
const li = document.createElement("li");
li.id = newTodo.id;  // 고유 ID 적용
li.innerText = newTodo.text;
```

## 삭제 기능 개선
- 삭제 버튼 클릭 시 `li.id` 값을 가져와 해당 ID를 가진 항목을 배열에서 제거

```javascript
function deleteTodo(event) {
  const li = event.target.parentElement;
  const idToDelete = parseInt(li.id);
  
  todos = todos.filter(todo => todo.id !== idToDelete);
  saveToLocalStorage();
  li.remove();
}
```