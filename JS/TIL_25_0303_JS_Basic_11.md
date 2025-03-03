# JavaScript LocalStorage 활용

## 개요
- `localStorage`를 사용하면 브라우저에 데이터를 저장하고 유지할 수 있음
- 페이지를 새로고침하거나 브라우저를 종료해도 데이터가 유지됨
- `key-value` 형태로 문자열 데이터를 저장

## 기본 개념
- `localStorage.setItem(key, value)`: 데이터 저장
- `localStorage.getItem(key)`: 데이터 조회
- `localStorage.removeItem(key)`: 특정 데이터 삭제
- `localStorage.clear()`: 모든 데이터 삭제

## 코드 흐름
1. **HTML 기본 구조**
   - 입력 폼과 제목 태그 (`h1`)가 존재
   - 초기 상태에서 CSS `hidden` 클래스로 숨김 처리

2. **JavaScript로 LocalStorage 활용**
   - `localStorage`에서 `username`을 검색
   - 존재하면 `h1` 태그에 사용자 이름을 표시
   - 존재하지 않으면 로그인 폼을 표시하고 입력값을 저장

```javascript
const loginForm = document.getElementById("login-form");
const loginInput = document.getElementById("username");
const greeting = document.getElementById("greeting");
const USERNAME_KEY = "username";

function paintGreeting(username) {
    greeting.innerText = `Hello, ${username}!`;
    greeting.classList.remove("hidden");
}

function onLoginSubmit(event) {
    event.preventDefault();
    loginForm.classList.add("hidden");
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username);
    paintGreeting(username);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if (savedUsername === null) {
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit", onLoginSubmit);
} else {
    paintGreeting(savedUsername);
}
```

## 동작 과정
1. 페이지 로드 시 `localStorage`에서 `username`을 검색
2. `username`이 존재하면 환영 메시지를 표시
3. `username`이 없으면 로그인 폼을 표시
4. 로그인 폼 제출 시 입력값을 `localStorage`에 저장하고 화면 업데이트
5. 새로고침해도 저장된 `username`이 유지되어 자동으로 환영 메시지를 표시

## 최적화
- `paintGreeting` 함수에서 `username`을 매개변수로 받지 않고 직접 `localStorage`에서 가져올 수도 있음
- `localStorage` 조회 횟수를 줄이려면 변수에 저장하여 재사용 가능

```javascript
function paintGreeting() {
    const username = localStorage.getItem(USERNAME_KEY);
    if (username) {
        greeting.innerText = `Hello, ${username}!`;
        greeting.classList.remove("hidden");
    }
}
```

## 마무리
- `localStorage`는 간단한 사용자 정보를 저장하는 데 유용함
- 입력값을 저장하고 불러와 자동 로그인처럼 활용 가능
- 브라우저 종료 후에도 유지되므로 장기적인 데이터 저장 가능

