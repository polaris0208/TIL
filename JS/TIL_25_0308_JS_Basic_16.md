# 랜덤 배경 이미지 적용하기

## 개념 정리
- JavaScript를 사용하여 웹페이지에 랜덤 배경 이미지를 추가하는 방법을 학습한다.
- `createElement()`를 활용하여 `img` 요소를 동적으로 생성한다.
- `Math.random()`과 `Math.floor()`를 사용하여 랜덤한 숫자를 생성한다.
- 생성된 `img` 요소를 `appendChild()`를 이용하여 `body`에 추가한다.

## 실행과정
- `background.js` 파일을 생성하고 `index.html`에 포함시킨다.
- `img` 폴더에 배경 이미지 파일을 저장하고 파일명을 배열로 관리한다.
- JavaScript에서 랜덤한 숫자를 생성하여 이미지 파일을 선택한다.
- 선택된 이미지를 `img` 요소로 생성하고 `src` 속성을 설정한다.
- `document.body.appendChild()`를 사용하여 HTML 문서에 추가한다.

## `background.js`

```javascript
// 이미지 파일 배열
const images = ["0.jpeg", "1.jpeg", "2.jpeg"];

// 랜덤한 숫자 생성 (0 ~ 2)
const chosenImage = images[Math.floor(Math.random() * images.length)];

// img 요소 생성
const bgImage = document.createElement("img");

// 이미지 경로 설정
bgImage.src = `img/${chosenImage}`;

// body에 추가
document.body.appendChild(bgImage);
```

## 실행 방식
1. `index.html`을 브라우저에서 실행한다.
2. 페이지를 새로고침할 때마다 다른 배경 이미지가 나타난다.
3. 이미지 파일이 `img` 폴더에 존재해야 정상적으로 동작한다.

