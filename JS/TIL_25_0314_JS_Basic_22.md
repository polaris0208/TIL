# To-Do 리스트 불러오기 2

## JavaScript 객체를 문자열로 변환 및 복원
- JavaScript 객체(배열 포함)를 문자열로 변환 가능
- `JSON.stringify()`를 사용하여 객체 → 문자열 변환
- `JSON.parse()`를 사용하여 문자열 → 객체 복원

```javascript
const todos = ["할 일 1", "할 일 2"];
const todosString = JSON.stringify(todos);
console.log(todosString); // "[\"할 일 1\", \"할 일 2\"]"

const parsedTodos = JSON.parse(todosString);
console.log(parsedTodos); // ["할 일 1", "할 일 2"]
```

## 배열 요소를 하나씩 처리하는 방법
- 배열의 각 요소에 대해 함수를 실행하는 방법 두 가지
  1. 화살표 함수 사용
  2. 일반 함수 사용

```javascript
const todos = ["할 일 1", "할 일 2", "할 일 3"];

todos.forEach((item) => console.log(item)); // 화살표 함수

todos.forEach(function (item) {
    console.log(item); // 일반 함수
});
```

## `paintToDo` 함수로 리스트 표시
- `console.log()` 대신 `paintToDo()` 함수를 사용하여 화면에 표시

```javascript
function paintToDo(todo) {
    const li = document.createElement("li");
    li.innerText = todo;
    document.body.appendChild(li);
}

const todos = ["할 일 A", "할 일 B", "할 일 C"];
todos.forEach(paintToDo);
```

## 기존 To-Do 리스트 유지 문제
- 새 할 일을 추가할 때 기존 목록을 유지하지 않는 문제 발생
- `localStorage`에서 기존 목록을 불러오도록 수정

```javascript
let todos = [];
const savedTodos = localStorage.getItem("todos");
if (savedTodos) {
    todos = JSON.parse(savedTodos);
}

function saveToDos() {
    localStorage.setItem("todos", JSON.stringify(todos));
}
```

## 해결 방법: 기존 To-Do와 새로운 To-Do 병합
- 기존 `todos` 배열을 유지하고 새 할 일을 추가하도록 변경

```javascript
function addNewToDo(newTodo) {
    todos.push(newTodo);
    saveToDos();
    paintToDo(newTodo);
}
```

## 삭제 기능 문제
- 현재 삭제 버튼이 `localStorage`에서 데이터를 제거하지 않음
- `localStorage`에서도 삭제되도록 수정 필요

```javascript
function deleteToDo(todo) {
    todos = todos.filter((item) => item !== todo);
    saveToDos();
}
