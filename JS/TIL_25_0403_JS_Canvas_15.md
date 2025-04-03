## 캔버스에 텍스트 추가하기

### 개요
- 사용자가 입력한 텍스트를 캔버스(double-click)에서 지정한 위치에 표시
- JavaScript의 `canvas` API와 이벤트 리스너 활용

### 주요 개념
#### 1. 입력 필드 생성
- `input` 요소를 추가하고 `id="text"` 설정
- JavaScript에서 `getElementById("text")`로 참조

```html
<input type="text" id="text" placeholder="Write and then double click" />
```

```javascript
const textInput = document.getElementById("text");
```

#### 2. 더블 클릭 이벤트 리스너 등록
- `canvas.addEventListener("dblclick", callbackFunction)`
- `event.offsetX`, `event.offsetY`로 클릭 위치 확인

```javascript
canvas.addEventListener("dblclick", (event) => {
    console.log(event.offsetX, event.offsetY);
});
```

#### 3. 입력된 텍스트를 캔버스에 표시
- `context.strokeText(text, x, y)` 또는 `context.fillText(text, x, y)` 활용
- `textInput.value`에서 사용자 입력값 가져오기

```javascript
const text = textInput.value;
context.strokeText(text, event.offsetX, event.offsetY);
```

#### 4. 컨텍스트 상태 저장 및 복원
- `context.save()`를 사용하여 기존 스타일 저장
- 텍스트 추가 후 `context.restore()`로 원래 상태 복원

```javascript
context.save();
context.lineWidth = 1;
context.strokeText(text, event.offsetX, event.offsetY);
context.restore();
```

#### 5. 입력값 검증
- 입력 필드가 비어 있으면 실행하지 않도록 조건 추가

```javascript
if (text !== "") {
    context.strokeText(text, event.offsetX, event.offsetY);
}
```

#### 6. 폰트 스타일 변경
- `context.font = "48px serif"`로 크기 및 폰트 지정
- `strokeText`와 `fillText`의 차이점 설명

```javascript
context.font = "48px serif";
context.fillText(text, event.offsetX, event.offsetY);
```

#### 7. 선 끝 스타일 변경
- `context.lineCap = "round"` 설정으로 부드러운 마감 처리

```javascript
context.lineCap = "round";
```

### 정리
- 더블 클릭 이벤트를 활용하여 캔버스에 텍스트 추가
- `context.save()` 및 `context.restore()`로 원래 상태 유지
- `strokeText()`와 `fillText()`를 활용하여 원하는 스타일 적용
- 입력값이 없을 경우 처리하는 로직 추가
- 폰트 및 선 마감 스타일을 변경하여 가독성을 높임

