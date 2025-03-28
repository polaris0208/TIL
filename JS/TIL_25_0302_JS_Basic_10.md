# 로컬 스토리지에서 사용자명 불러오기

## 개요
- 로컬 스토리지에 저장된 사용자명을 확인하여 로그인 폼 또는 환영 메시지를 표시하는 기능 구현
- 사용자명이 존재하면 환영 메시지를, 없으면 로그인 폼을 표시
- 문자열 반복을 줄이기 위해 상수 사용
- 코드 정리를 위해 별도의 함수 활용

## 로컬 스토리지에서 사용자명 확인

```javascript
const savedUsername = localStorage.getItem("username");
console.log(savedUsername); // 저장된 사용자명이 없으면 null 반환
```

## 문자열 상수 사용

```javascript
const USERNAME_KEY = "username";
const savedUsername = localStorage.getItem(USERNAME_KEY);
```
- `USERNAME_KEY`를 상수로 정의하여 문자열 오타 방지

## 폼과 환영 메시지 초기 상태 설정

```javascript
document.querySelector("#login-form").classList.add("hidden");
document.querySelector("#greeting").classList.add("hidden");
```
- 초기에 폼과 환영 메시지를 숨김

## 사용자명에 따라 UI 변경
- 사용자명이 없으면 로그인 폼을 표시, 있으면 환영 메시지 출력

```javascript
if (savedUsername === null) {
    document.querySelector("#login-form").classList.remove("hidden");
} else {
    paintGreetings(savedUsername);
}
```


## 환영 메시지 표시 함수
- 사용자명을 받아 환영 메시지를 표시하는 함수

```javascript
function paintGreetings(username) {
    const greeting = document.querySelector("#greeting");
    greeting.innerText = `Hello, ${username}!`;
    greeting.classList.remove("hidden");
}
```


## 로그인 폼 이벤트 리스너 추가
- 로그인 폼 제출 시 사용자명을 저장하고 환영 메시지 표시

```javascript
document.querySelector("#login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.querySelector("#username-input").value;
    localStorage.setItem(USERNAME_KEY, username);
    paintGreetings(username);
});
```

## 최종 테스트
- 사용자명이 없는 경우 로그인 폼이 표시됨
- 로그인 후 사용자명이 저장되며 환영 메시지가 나타남
- 새로고침 후에도 사용자명이 유지됨
