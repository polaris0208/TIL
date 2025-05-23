# JavaScript 입력값 처리

## 사용자 입력값 받기
- 사용자에게 이름을 입력받아 화면에 표시하는 기능 구현
- HTML에서 `<input>` 및 `<button>` 요소 생성
- HTML 기본 구조 작성

## JavaScript에서 요소 선택하기

```javascript
const loginForm = document.getElementById("login-form");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
```

## 이벤트 리스너 추가 (버튼 클릭 시 동작)

```javascript
loginButton.addEventListener("click", function() {
    console.log("Button clicked");
});
```

## 입력값 가져오기

```javascript
loginButton.addEventListener("click", function() {
    console.log(loginInput.value);
});
```

## 입력값 검증 (빈 값 방지)

```javascript
loginButton.addEventListener("click", function() {
    const name = loginInput.value;
    if (name === "") {
        alert("이름을 입력하세요.");
    } else {
        console.log("사용자 입력: ", name);
    }
});
```

## 요약
- HTML에서 `<input>`과 `<button>` 생성
- JavaScript에서 요소 선택 및 이벤트 리스너 추가
- `input.value`로 사용자 입력값 가져오기
- 입력값이 비어있을 경우 검증 추가