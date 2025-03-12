# To-Do 저장 기능

## 개요
- 브라우저 새로고침 시 To-Do 리스트가 사라지는 문제 해결
- `localStorage`를 이용하여 To-Do 리스트 저장 및 불러오기 구현

## 주요 개념
- `localStorage`는 문자열만 저장 가능
- JavaScript 객체나 배열을 저장하려면 `JSON.stringify()` 사용
- 저장된 데이터를 다시 사용할 때는 `JSON.parse()`로 변환 필요

## 구현 단계
### 1. To-Do 리스트 배열 생성

```javascript
const todos = [];
```

### 2. 새로운 To-Do 추가 및 배열에 저장

```javascript
function addTodo(text) {
    todos.push(text);
    saveTodos();
}
```

### 3. `localStorage`에 저장

```javascript
function saveTodos() {
    localStorage.setItem("todos", JSON.stringify(todos));
}
```

### 4. 저장된 To-Do 불러오기

```javascript
function loadTodos() {
    const savedTodos = localStorage.getItem("todos");
    if (savedTodos) {
        todos.push(...JSON.parse(savedTodos));
        renderTodos();
    }
}
```

### 5. 화면에 To-Do 리스트 표시

```javascript
function renderTodos() {
    todos.forEach(todo => {
        console.log(todo); // 화면에 표시하는 로직 추가 가능
    });
}
```

## 정리
- `localStorage.setItem("key", value)`: 데이터 저장
- `localStorage.getItem("key")`: 데이터 가져오기
- `JSON.stringify(object)`: 객체를 문자열로 변환
- `JSON.parse(string)`: 문자열을 객체로 변환