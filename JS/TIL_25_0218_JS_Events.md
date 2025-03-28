# JavaScript 이벤트

## JavaScript와 HTML 연동
- JavaScript는 HTML을 통해 `document` 객체에 접근 가능
- `app.js`가 HTML에서 불러와져야 JavaScript 코드가 동작함

## HTML 요소 선택 방법
- JavaScript에서 HTML 요소를 선택하는 여러 방법 존재
- 주요 메서드:

  ```js
  document.getElementById("id명");
  document.getElementsByClassName("class명");
  document.getElementsByTagName("태그명");
  document.querySelector("선택자");
  document.querySelectorAll("선택자");
  ```

- `querySelector`가 가장 유용함 (CSS 선택자 사용 가능)

  ```js
  const title = document.querySelector(".hello h1");
  ```

## 요소의 속성 접근 및 변경
- `console.log(element)` 요소 출력
- `console.dir(element)` 요소의 속성을 객체 형태로 출력
- 스타일 변경 예제:

  ```js
  const title = document.querySelector("h1");
  title.style.color = "blue"; // 글자색을 파란색으로 변경
  ```

## 이벤트(Event) 개념
- 이벤트: 사용자의 특정 동작 (클릭, 키 입력, 마우스 이동 등)
- 주요 이벤트 예시:
  - `click`: 클릭 이벤트
  - `mouseenter`: 마우스가 요소 위에 올라왔을 때
  - `mouseleave`: 마우스가 요소에서 벗어날 때
  - `keydown`: 키보드 키가 눌렸을 때
  - `load`: 페이지가 로드될 때

## 이벤트 리스너 추가
- `addEventListener("이벤트명", 실행할 함수)` 사용

  ```js
  const title = document.querySelector("h1");
  function handleTitleClick() {
      console.log("제목이 클릭됨");
  }
  title.addEventListener("click", handleTitleClick);
  ```

- 클릭하면 `handleTitleClick` 함수 실행됨

## 이벤트 리스너를 활용한 스타일 변경
- 클릭하면 글자색 변경하는 코드:

  ```js
  const title = document.querySelector("h1");
  function handleTitleClick() {
      title.style.color = "blue";
  }
  title.addEventListener("click", handleTitleClick);
  ```

## 이벤트 리스너 함수 전달 방식 주의점
- 함수 실행 시 `()`를 붙이면 즉시 실행됨 (원하지 않는 동작)

  ```js
  title.addEventListener("click", handleTitleClick); // 올바른 방식
  title.addEventListener("click", handleTitleClick()); // 잘못된 방식 (즉시 실행됨)
  ```

## 정리
- JavaScript는 HTML과 연동하여 요소를 선택하고 수정 가능
- `querySelector`를 활용하면 CSS 선택자로 요소 검색 가능
- 이벤트 리스너를 사용하여 사용자 동작을 감지하고 반응 가능
- `addEventListener`를 사용하여 특정 이벤트 발생 시 함수 실행 가능