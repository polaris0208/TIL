## 캔버스 초기화 및 지우개 기능 구현

### 캔버스 초기화 (Reset)
- 사용자가 버튼을 클릭하면 캔버스를 초기 상태로 되돌림
- 해결 방법: 캔버스 전체를 흰색으로 덮어 기존 내용을 지움
- 코드 구현

```html
<button id="destroy-btn">Destroy</button>
<canvas id="canvas" width="800" height="800"></canvas>
```

```javascript
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const destroyBtn = document.getElementById("destroy-btn");
const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 800;

destroyBtn.addEventListener("click", () => {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
});
```

### 지우개 모드 (Eraser Mode)
- 지우개 모드는 배경색과 같은 색(흰색)으로 그리는 방식으로 구현
- 사용자가 버튼을 클릭하면 선 색상을 흰색으로 변경
- 만약 채우기 모드일 경우, 자동으로 일반 드로잉 모드로 변경
- 코드 구현

```html
<button id="eraser-btn">Eraser</button>
```

```javascript
const eraserBtn = document.getElementById("eraser-btn");
let isFilling = false;

eraserBtn.addEventListener("click", () => {
    ctx.strokeStyle = "white";
    isFilling = false; // 채우기 모드 해제
    eraserBtn.innerText = "Eraser Mode";
});
```

### 기능 테스트
- 초기화 버튼 클릭 시 캔버스가 완전히 지워지는지 확인
- 지우개 버튼 클릭 후 기존 그림 위를 드로잉하여 삭제 효과 확인
- 지우개 모드에서 다시 색상을 변경하면 정상적으로 색이 칠해지는지 확인