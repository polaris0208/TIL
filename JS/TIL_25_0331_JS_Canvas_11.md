# 색상 선택 기능 구현 2

## 개요
- 사용자가 직접 색상을 입력하는 대신, 미리 정의된 색상을 제공
- 색상 선택 시 즉시 적용되도록 구현
- 사용자 경험을 개선하기 위해 클릭한 색상을 시각적으로 피드백 제공

## 구현 과정

### 1. HTML에 색상 옵션 추가
- `div` 요소를 사용하여 색상 선택 버튼 생성
- `data-color` 속성을 활용해 색상 정보를 저장

```html
<div class="color-option" data-color="#3498db" style="background-color: #3498db;"></div>
<div class="color-option" data-color="#e74c3c" style="background-color: #e74c3c;"></div>
```

### 2. CSS 스타일 적용
- 선택 버튼을 클릭할 수 있도록 스타일 지정
- 크기와 커서를 설정하여 버튼처럼 보이도록 함

```css
.color-option {
  width: 50px;
  height: 50px;
  cursor: pointer;
  display: inline-block;
  margin: 5px;
}
```

### 3. JavaScript로 색상 선택 기능 추가
- 모든 색상 옵션을 가져와 클릭 이벤트 추가
- `data-color` 속성에서 색상 값을 가져와 적용

```javascript
const colorOptions = Array.from(document.getElementsByClassName("color-option"));

colorOptions.forEach(color => {
  color.addEventListener("click", event => {
    const selectedColor = event.target.dataset.color;
    changeColor(selectedColor);
  });
});

function changeColor(color) {
  console.log("선택된 색상:", color);
  document.getElementById("color-input").value = color;
}
```

### 4. 클릭 시 피드백 제공
- 사용자가 선택한 색상을 입력 필드에 반영하여 변경 사항을 시각적으로 확인 가능하도록 함

```javascript
document.getElementById("color-input").value = color;
```

## 정리
- `data-color` 속성을 활용해 색상을 저장하고 JavaScript에서 활용
- `getElementsByClassName`을 사용하여 요소를 가져오고, `Array.from()`을 사용해 배열로 변환 후 `forEach` 적용
- 클릭 이벤트를 추가하여 선택된 색상을 적용하고 사용자에게 피드백 제공

