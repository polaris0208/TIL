# CSS와 JavaScript의 역할 분리

## 개요
- 스타일은 CSS에서, 애니메이션은 JavaScript에서 처리하는 것이 최적의 방법
- JavaScript 내부에 CSS 스타일을 작성하는 것은 바람직하지 않음

## HTML, CSS, JavaScript의 연계
- `index.html`에서 CSS와 JavaScript 파일을 불러옴
- CSS에서 `h1` 요소의 기본 색상을 `blue`로 설정
- 새로운 클래스 `.active`를 정의하여 `tomato` 색상을 적용

```css
/* styles.css */
h1 {
  color: blue;
}

.active {
  color: tomato;
  transition: color 0.5s ease-in-out;
}
```

## JavaScript에서 클래스 추가 및 제거
- `h1` 요소에 `.active` 클래스를 추가하여 색상을 변경
- 클릭 시 `active` 클래스를 추가/제거하여 토글 기능 구현

```js
// script.js
const h1 = document.querySelector("h1");

h1.addEventListener("click", () => {
  if (h1.className === "active") {
    h1.className = ""; // 클래스 제거
  } else {
    h1.className = "active"; // 클래스 추가
  }
});
```

## 코드 개선 (하드코딩 방지)
- 문자열을 직접 사용하는 대신 상수(Constant)로 저장하여 오류 방지

```js
const CLICKED_CLASS = "active";

h1.addEventListener("click", () => {
  if (h1.className === CLICKED_CLASS) {
    h1.className = "";
  } else {
    h1.className = CLICKED_CLASS;
  }
});
```

## 기존 클래스 유지 문제 해결
- 기존의 `className`을 통째로 변경하는 대신 `classList` 사용

```js
h1.addEventListener("click", () => {
  h1.classList.toggle("active");
});
```

## 결론
- JavaScript는 직접 스타일을 변경하지 않고, HTML의 클래스를 조작하는 방식이 최적
- `classList.toggle()`을 활용하여 코드 가독성을 높이고 유지보수를 용이하게 함
