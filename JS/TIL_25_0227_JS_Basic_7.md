# 이벤트 처리 및 preventDefault 정리

## 기본 개념
- HTML의 기본 동작(예: 링크 클릭 시 페이지 이동)을 JavaScript에서 제어 가능
- `addEventListener`를 사용하여 이벤트 리스너를 추가
- `preventDefault()`를 사용하여 브라우저의 기본 동작을 막을 수 있음

## JavaScript 이벤트 리스너 추가
- 클릭 시 `alert("클릭됨!")`이 실행됨
- 하지만 기본 동작(페이지 이동)은 그대로 유지됨

```javascript
const link = document.querySelector("#myLink");

link.addEventListener("click", function(event) {
    alert("클릭됨!");
});
```

## 기본 동작 막기 (preventDefault)
- `event.preventDefault();`를 호출하면 링크가 페이지를 이동하지 않음
- 경고창만 표시됨

```javascript
const link = document.querySelector("#myLink");

link.addEventListener("click", function(event) {
    event.preventDefault(); // 기본 동작 막기
    alert("기본 동작이 방지되었습니다!");
});
```

## 이벤트 객체 (Event Object)
- 이벤트 핸들러 함수의 첫 번째 매개변수로 이벤트 객체 전달됨
- 이벤트 객체를 사용하면 다양한 정보를 얻을 수 있음
  - `event.type`: 이벤트 유형 (예: "click")
  - `event.clientX`, `event.clientY`: 클릭한 위치의 X, Y 좌표

```javascript
link.addEventListener("click", function(event) {
    event.preventDefault();
    console.log(event.type); // "click"
    console.log(event.clientX, event.clientY); // 클릭한 좌표 출력
});
```

## 정리
- `addEventListener("이벤트 유형", 함수)`: 특정 이벤트가 발생할 때 실행될 함수 등록
- `preventDefault()`: 기본 동작(예: 링크 이동, 폼 제출 등) 방지
- 이벤트 객체 활용: `event.type`, `event.clientX`, `event.clientY` 등 다양한 정보 접근 가능