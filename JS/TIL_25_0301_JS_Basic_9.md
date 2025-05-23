# 로컬 스토리지 사용자 이름 저장

## 개요
- 사용자가 입력한 이름을 저장하고 페이지를 새로고침해도 유지되도록 함
- `localStorage` API를 활용하여 데이터를 브라우저에 저장하고 불러옴
- HTML, CSS, JavaScript를 활용하여 동적 UI 구성

## 주요 개념
### 기본 폼 동작 및 숨김 처리
- `h1` 요소와 `form` 요소를 사용하여 사용자 입력을 받음
- `h1` 요소는 기본적으로 숨겨져 있음 (`display: none` 적용)
- 폼 제출 시 기본 동작을 막고 (`preventDefault`), 폼을 숨기고 `h1`을 표시함

### 사용자 이름 저장
- 입력된 사용자 이름을 `localStorage`에 저장
- `localStorage.setItem("username", username)` 사용

### 사용자 이름 불러오기
- 저장된 사용자 이름이 있으면 폼을 숨기고 `h1`을 표시
- `localStorage.getItem("username")` 사용

### 사용자 이름 삭제
- 필요 시 `localStorage.removeItem("username")`을 사용하여 삭제 가능

## 예시

### JavaScript
```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-input");
const greeting = document.querySelector("#greeting");
const USERNAME_KEY = "username";

function onLoginSubmit(event) {
    event.preventDefault();
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    showGreeting(username);
}

function showGreeting(username) {
    greeting.textContent = `안녕하세요, ${username}!`;
    greeting.classList.remove("hidden");
    loginForm.classList.add("hidden");
}

const savedUsername = localStorage.getItem(USERNAME_KEY);
if (savedUsername) {
    showGreeting(savedUsername);
} else {
    loginForm.addEventListener("submit", onLoginSubmit);
}
```

## 정리
- `localStorage`를 사용하면 데이터를 브라우저에 저장하여 새로고침 후에도 유지 가능
- `setItem()`, `getItem()`, `removeItem()`을 활용하여 저장, 불러오기, 삭제 기능 구현
- 폼과 `h1` 요소를 동적으로 조작하여 사용자 경험 개선

