### CSS 개념 정리 및 예시

#### CSS Reset

- 브라우저 기본 스타일을 제거해 일관성 유지  
- `reset.css`를 import하여 사용

```css
/* 예시 */
@import url("https://meyerweb.com/eric/tools/css/reset/reset.css");
```

#### Flexbox 레이아웃

- `display: flex`로 요소 정렬  
- `justify-content`, `align-items`, `gap` 등 사용

```css
body {
  display: flex;
  gap: 20px;
  justify-content: space-between;
  align-items: flex-start;
}
```

#### 배경, 테두리, 여백 설정

- `background-color`, `border-radius`, `padding` 사용

```css
body {
  background-color: gainsboro;
  padding: 20px;
}

canvas {
  background-color: white;
  border-radius: 10px;
}
```

#### 요소 정렬을 위한 래퍼(div)

- 버튼이나 input 그룹을 감싸기 위해 `div` 사용  
- 컬럼 방향 정렬

```css
.btns {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
```

#### 컬러 옵션 UI 디자인

- 컬러를 동그랗게 표시, 호버 효과 추가

```css
.color-options {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.color-option {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 5px solid white;
  transition: transform 0.1s ease-in-out;
}

.color-option:hover {
  transform: scale(1.2);
}
```

#### 버튼 초기화 및 재디자인

- 기본 스타일 제거: `all: unset`  
- 새롭게 스타일 지정

```css
button {
  all: unset;
  padding: 10px 0;
  background-color: royalblue;
  color: white;
  font-weight: 500;
  border-radius: 10px;
  cursor: pointer;
  text-align: center;
  transition: opacity 0.2s linear;
}

button:hover {
  opacity: 0.85;
}
```

#### input 및 placeholder 스타일링

```css
#text {
  all: unset;
  text-align: center;
  font-weight: 500;
  background-color: white;
  border-radius: 10px;
}

#text::placeholder {
  color: gray;
}
```

#### 파일 업로드 버튼 디자인

- `<label>` 클릭 시 `<input type="file">` 트리거  
- `display: none`으로 input 숨김

```html
<label for="file">📎 사진 추가</label>
<input type="file" id="file" style="display: none;" />
```

#### 기타 팁

- `font-family` 설정으로 시스템 폰트 적용 가능

```css
body {
  font-family: system-ui, sans-serif;
}
```
