## 이벤트(Event)
- 웹 브라우저에서 특정 동작(클릭, 입력, 스크롤 등)이 발생하는 것.
- 이벤트 발생 시 특정 동작(함수 실행 등)을 수행하도록 설정 가능.

## 이벤트 리스너(Event Listener)
- 특정 이벤트가 발생했을 때 실행할 함수를 지정하는 메커니즘.
- `addEventListener()` 메서드를 사용하여 이벤트를 감지하고 처리.

## 기본적인 이벤트 리스너 예제

```javascript
// 버튼 클릭 시 메시지를 출력하는 예제
const button = document.querySelector("#myButton");
button.addEventListener("click", function() {
    console.log("버튼이 클릭되었습니다!");
});
```

## 이벤트 리스너의 기본 동작
- 특정 HTML 요소에 이벤트 리스너를 추가하면, 해당 이벤트가 발생할 때마다 지정된 함수가 실행됨.
- `addEventListener`는 이벤트 유형과 실행할 함수를 매개변수로 받음.

## 이벤트 객체 (Event Object)
- 이벤트 발생 시 브라우저가 자동으로 이벤트 객체를 생성하여 핸들러 함수에 전달.
- 이벤트 객체를 활용하면, 발생한 이벤트의 세부 정보 확인 가능.

```javascript
// 마우스 클릭 이벤트에서 좌표 정보 출력
button.addEventListener("click", function(event) {
    console.log(`X 좌표: ${event.clientX}, Y 좌표: ${event.clientY}`);
});
```

## 기본 동작 방지 (preventDefault)
- 일부 이벤트(예: 폼 제출, 링크 클릭 등)는 기본 동작이 설정되어 있음.
- `preventDefault()` 메서드를 사용하여 기본 동작을 막을 수 있음.

```javascript
// 폼 제출 시 새로고침 방지
const form = document.querySelector("#myForm");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    console.log("폼 제출 이벤트 발생, 하지만 새로고침은 안 됨.");
});
```

## 이벤트 전파 (Event Bubbling & Capturing)
- 이벤트는 부모 요소까지 전파되는 특성이 있음.
- `event.stopPropagation()`을 사용하여 이벤트 전파를 중단할 수 있음.

```javascript
// 이벤트 전파 중지 예제
const parent = document.querySelector("#parent");
const child = document.querySelector("#child");

child.addEventListener("click", function(event) {
    event.stopPropagation(); // 부모 요소로의 전파 방지
    console.log("자식 요소 클릭");
});

parent.addEventListener("click", function() {
    console.log("부모 요소 클릭");
});
```

## 이벤트 리스너 제거
- `removeEventListener()`를 사용하여 특정 이벤트 리스너를 제거할 수 있음.
- 단, `addEventListener()`에 전달한 함수와 같은 함수를 지정해야만 제거됨.

```javascript
// 이벤트 리스너 제거 예제
function handleClick() {
    console.log("클릭 이벤트 발생");
}

button.addEventListener("click", handleClick);
// 이후 특정 조건에서 이벤트 제거 가능
button.removeEventListener("click", handleClick);
```

## 이벤트 위임 (Event Delegation)
- 여러 개의 자식 요소에 개별적으로 이벤트 리스너를 추가하는 대신, 부모 요소에서 감지하는 방식.
- 성능 최적화에 유용함.

```javascript
// 이벤트 위임을 이용한 리스트 항목 클릭 감지
const list = document.querySelector("#myList");
list.addEventListener("click", function(event) {
    if (event.target.tagName === "LI") {
        console.log(`클릭된 항목: ${event.target.textContent}`);
    }
});
```

##  결론
- 이벤트 리스너는 웹 개발에서 필수적인 개념이며, 다양한 방식으로 활용 가능.
- `preventDefault()`, `stopPropagation()`, `removeEventListener()` 등을 적절히 사용하여 원하는 동작을 제어할 수 있음.
- 이벤트 위임을 활용하면 성능 최적화가 가능함.