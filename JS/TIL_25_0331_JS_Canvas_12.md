# 캔버스 모드 전환 
> 드로잉 모드 / 채우기 모드

## 개념 정리

- **목표**: 버튼을 클릭하면 캔버스가 드로잉 모드에서 채우기 모드로 전환됨.
- **구성 요소**
  - 버튼을 생성하여 모드를 변경하는 역할 수행.
  - JavaScript에서 버튼 요소를 가져와 클릭 이벤트를 추가.
  - `isFilling` 변수를 사용하여 현재 모드 추적.
  - 채우기 모드일 때 클릭하면 전체 캔버스가 특정 색으로 채워짐.
- **이벤트 흐름**
  - 버튼 클릭 → `isFilling` 값 변경 → 버튼 텍스트 변경
  - 캔버스 클릭 → 현재 모드에 따라 드로잉 또는 채우기 실행

## 코드 예시

### HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>캔버스 모드 전환</title>
</head>
<body>
    <button id="mode-btn">Fill</button>
    <canvas id="canvas" width="800" height="800" style="border:1px solid black;"></canvas>
    <script src="script.js"></script>
</body>
</html>
```

### JavaScript

```javascript
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const modeBtn = document.getElementById("mode-btn");

let isFilling = false;

modeBtn.addEventListener("click", () => {
    isFilling = !isFilling;
    modeBtn.innerText = isFilling ? "Draw" : "Fill";
});

canvas.addEventListener("click", () => {
    if (isFilling) {
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
});

let painting = false;
canvas.addEventListener("mousedown", () => { painting = true; });
canvas.addEventListener("mouseup", () => { painting = false; });
canvas.addEventListener("mousemove", (event) => {
    if (!painting || isFilling) return;
    ctx.lineTo(event.offsetX, event.offsetY);
    ctx.stroke();
});
```

## 실행 흐름

1. **버튼 클릭 시 모드 전환**
   - `isFilling` 값 변경 (`true` ↔ `false`)
   - 버튼 텍스트 변경 ("Fill" ↔ "Draw")

2. **캔버스 클릭 시 동작**
   - `isFilling`이 `true`이면 전체 캔버스를 채우는 사각형 생성
   - `isFilling`이 `false`이면 기존처럼 드로잉 모드 유지

3. **마우스 이동 시 드로잉 모드 작동**
   - 마우스 클릭한 상태에서 이동하면 선이 그려짐
   - `isFilling` 모드일 때는 드로잉 비활성화

## 결과

- 버튼을 클릭하여 "Fill" 또는 "Draw" 모드를 전환 가능
- "Fill" 모드에서 캔버스를 클릭하면 현재 색상으로 전체 캔버스 채우기
- "Draw" 모드에서 마우스를 움직이며 선을 그림
- 간단한 이벤트 리스너 조합으로 드로잉/채우기 기능 구현