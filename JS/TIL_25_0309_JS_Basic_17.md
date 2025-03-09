# To-Do List

## 개요
- JavaScript를 사용하여 To-Do List를 구현하는 과정 정리
- HTML의 폼(form)과 리스트(ul)를 활용하여 사용자 입력을 처리
- JavaScript로 이벤트 리스너를 추가하여 동작 구현

## 기본 구조
- `index.html`에서 폼과 리스트를 생성
- JavaScript에서 DOM 요소를 가져와 이벤트 리스너 추가
- 입력값을 받아 리스트에 추가하는 기능 구현

## JavaScript 코드

```javascript
// HTML 요소 가져오기
const todoForm = document.getElementById("todo-form");
const todoInput = document.getElementById("todo-input");
const todoList = document.getElementById("todo-list");

// 폼 제출 이벤트 리스너 추가
todoForm.addEventListener("submit", function(event) {
    event.preventDefault(); // 페이지 새로고침 방지
    
    const newTodo = todoInput.value.trim(); // 입력값 저장
    if (newTodo === "") return; // 빈 값 처리
    
    addTodo(newTodo); // 할 일 추가 함수 호출
    todoInput.value = ""; // 입력 필드 초기화
});

// 할 일을 리스트에 추가하는 함수
function addTodo(todoText) {
    const li = document.createElement("li");
    li.textContent = todoText;
    todoList.appendChild(li);
}
```

## 주요 개념 정리
- **HTML 요소 가져오기**: `document.getElementById()`를 사용하여 폼, 입력 필드, 리스트 요소를 가져옴
- **이벤트 리스너 추가**: `addEventListener("submit", function(event) {...})`를 사용하여 폼 제출 시 동작 설정
- **기본 동작 방지**: `event.preventDefault();`를 사용하여 폼 제출 시 페이지 새로고침을 막음
- **입력값 가져오기**: `todoInput.value.trim();`을 사용하여 입력값을 가져오고 공백 제거
- **입력값이 비어 있는 경우 처리**: `if (newTodo === "") return;`을 사용하여 빈 문자열 입력 방지
- **새로운 리스트 아이템 추가**: `document.createElement("li")`를 사용하여 새로운 `<li>` 요소 생성 후 리스트에 추가
- **입력 필드 초기화**: `todoInput.value = "";`을 사용하여 입력 후 필드 비우기