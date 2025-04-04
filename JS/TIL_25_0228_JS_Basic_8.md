# 사용자명 입력

## 목표
- 사용자가 이름을 입력하면 폼을 숨기고, 환영 메시지를 표시
- `display: none`을 이용해 폼을 숨김
- JavaScript로 클래스 추가/제거
- 템플릿 리터럴 사용법 익히기

## 개념 정리
- `display: none`을 사용해 요소를 숨길 수 있음
- `classList.add("hidden")` → 폼을 숨김
- `classList.remove("hidden")` → h1을 표시
- `innerText = `Hello, ${username}!`` → 템플릿 리터럴로 문자열 결합
- `event.preventDefault();` → 기본 폼 제출 동작 방지

## JavaScript 코드

```js
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-input");
const greeting = document.querySelector("#greeting");
const HIDDEN_CLASS = "hidden";

loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const username = loginInput.value;
    loginForm.classList.add(HIDDEN_CLASS);
    greeting.innerText = `Hello, ${username}!`;
    greeting.classList.remove(HIDDEN_CLASS);
});
```