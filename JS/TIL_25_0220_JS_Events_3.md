# JavaScript 이벤트 개념 정리

## 이벤트(Event)란?
- 웹 페이지에서 사용자 동작(클릭, 입력, 창 크기 변경 등)에 반응하는 메커니즘
- 이벤트를 감지하고 특정 동작을 수행할 수 있음

## 이벤트 리스너 (Event Listener)
- 이벤트를 감지하고 실행할 함수를 지정하는 방법
- 대표적인 두 가지 방식
  1. `addEventListener()` 메서드 사용
  2. HTML 요소의 이벤트 속성(`onclick`, `onmouseenter` 등) 사용

### `addEventListener()` 방식 (권장)
```javascript
const title = document.querySelector("h1");
title.addEventListener("click", handleTitleClick);

function handleTitleClick() {
    alert("제목이 클릭되었습니다!");
}
```

### HTML 이벤트 속성 방식
```javascript
title.onclick = handleTitleClick;
```

- `addEventListener()`를 선호하는 이유:
  - `removeEventListener()`로 제거 가능
  - 여러 개의 이벤트 핸들러 추가 가능

## 윈도우(Window) 이벤트
- 브라우저 창과 관련된 이벤트 감지 가능

### `resize` 이벤트 (창 크기 변경 감지)
```javascript
window.addEventListener("resize", handleWindowResize);

function handleWindowResize() {
    document.body.style.backgroundColor = "tomato";
}
```

- 창 크기가 변경될 때 `body` 배경색을 `tomato`로 변경

## 클립보드 이벤트
- 사용자가 `copy`(복사) 이벤트를 실행할 때 감지

```javascript
window.addEventListener("copy", handleWindowCopy);

function handleWindowCopy() {
    alert("복사 감지됨!");
}
```

## 네트워크 상태 이벤트
- 온라인/오프라인 상태 감지 가능

### `offline` 이벤트 (인터넷 연결 끊김 감지)
```javascript
window.addEventListener("offline", handleWindowOffline);

function handleWindowOffline() {
    alert("⚠️ 인터넷 연결이 끊겼습니다!");
}
```

### `online` 이벤트 (인터넷 연결 복구 감지)
```javascript
window.addEventListener("online", handleWindowOnline);

function handleWindowOnline() {
    alert("인터넷 연결이 복구되었습니다!");
}
```

## 이벤트 리스너 패턴
1. 이벤트를 감지할 요소 선택 (`document.querySelector()` 등)
2. `addEventListener()`를 사용하여 이벤트 감지 설정
3. 특정 이벤트 발생 시 실행할 핸들러 함수 작성
4. 필요할 경우 `removeEventListener()`로 이벤트 제거 가능

## 결론
- 이벤트 리스너를 활용하면 다양한 사용자 입력에 반응할 수 있음
- `addEventListener()` 방식이 유연하고 유지보수에 유리
- 창 크기, 클립보드, 네트워크 상태 등 다양한 이벤트 감지 가능
