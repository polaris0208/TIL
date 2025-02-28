# **이벤트 개념 정리**

## **이벤트 확인 방법**
- 특정 HTML 요소에서 사용할 수 있는 이벤트를 확인하는 방법:
  - **MDN 검색**: `h1 mdn` 또는 `button mdn`과 같이 검색
  - **Web APIs 페이지 확인**: HTML 요소의 JavaScript API를 찾음
  - **개발자 도구(Console) 활용**: `console.dir(요소)` 실행하여 `on`으로 시작하는 이벤트 확인

## **주요 이벤트 종류**
- 다양한 이벤트가 존재하며, 대표적인 이벤트는 다음과 같음:
  - `click`: 요소를 클릭했을 때 실행
  - `mouseenter`: 마우스가 요소 위로 올라갈 때 실행
  - `mouseleave`: 마우스가 요소 밖으로 나갈 때 실행
  - `keydown`: 키보드를 누를 때 실행
  - `keyup`: 키보드를 눌렀다 뗄 때 실행
  - `scroll`: 사용자가 화면을 스크롤할 때 실행
  - `copy`: 사용자가 텍스트를 복사할 때 실행
  - `paste`: 사용자가 텍스트를 붙여넣을 때 실행

## **이벤트 리스너 추가 방법**
- JavaScript에서 `addEventListener` 메서드를 사용하여 이벤트를 추가할 수 있음

```javascript
const title = document.querySelector("h1");

title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
title.addEventListener("click", handleTitleClick);

function handleMouseEnter() {
    title.innerText = "마우스가 들어왔어요!";
}

function handleMouseLeave() {
    title.innerText = "마우스가 나갔어요!";
}

function handleTitleClick() {
    title.innerText = "제목이 클릭되었어요!";
}
```

## ** 이벤트 리스너 제거**
- 특정 조건에서 이벤트 리스너를 제거하려면 `removeEventListener` 사용

```javascript
title.removeEventListener("mouseenter", handleMouseEnter);
```

## **이벤트 활용 예제**
- 입력 필드에서 사용자가 입력할 때마다 콘솔에 값을 출력하는 예제

```javascript
const input = document.querySelector("input");

input.addEventListener("input", (event) => {
    console.log("현재 입력 값:", event.target.value);
});
```

## **이벤트와 CSS의 역할 분리**
- JavaScript에서 스타일을 변경할 수도 있지만, 가능하면 CSS에서 처리하는 것이 좋음
- 예제: 클래스를 추가하여 스타일 변경

```javascript
title.classList.add("highlight");
```

```css
.highlight {
    color: red;
    font-weight: bold;
}
```

## **정리**
- 이벤트는 HTML 요소에서 특정 동작이 발생했을 때 실행되는 기능
- `addEventListener`로 이벤트를 등록하고, 필요 시 `removeEventListener`로 제거 가능
- 다양한 이벤트를 활용하여 동적인 웹사이트 제작 가능