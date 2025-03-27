# 마우스 페인팅 개념 정리

## 개요
- 마우스 클릭과 이동을 이용하여 그림을 그리는 방법을 설명
- 마우스 이동만으로는 그림을 그리지 않고, 클릭을 눌렀을 때부터 선을 그림
- `moveTo`와 `lineTo`를 활용하여 브러시의 움직임을 제어

## 핵심 개념
- **moveTo(x, y)**: 브러시 위치를 이동 (선 없이 이동만 수행)
- **lineTo(x, y)**: 브러시 위치에서 지정한 좌표까지 선을 그림
- **stroke()**: 그려진 선을 화면에 표시
- **isPainting**: 마우스 클릭 여부를 확인하는 변수

## 이벤트 리스너 활용
### 마우스 이동 시 브러시 위치 이동

```javascript
canvas.addEventListener("mousemove", (event) => {
    if (!isPainting) {
        context.moveTo(event.offsetX, event.offsetY);
    } else {
        context.lineTo(event.offsetX, event.offsetY);
        context.stroke();
    }
});
```

### 마우스 클릭 시 그림 그리기 시작

```javascript
canvas.addEventListener("mousedown", () => {
    isPainting = true;
});
```

### 마우스 버튼을 떼면 그림 그리기 중지

```javascript
canvas.addEventListener("mouseup", () => {
    isPainting = false;
    context.beginPath(); // 새로운 경로 시작
});
```

## 버그 수정: 캔버스를 벗어나도 그림이 계속 그려지는 문제
- 마우스를 누른 상태에서 캔버스를 벗어나면 `mouseup` 이벤트가 발생하지 않음
- 해결 방법:
  - `mouseleave` 이벤트 추가하여 `isPainting`을 `false`로 변경
  - `document`의 `mouseup` 이벤트를 활용하여 모든 영역에서 마우스 버튼이 떼어질 때 `isPainting = false`

```javascript
document.addEventListener("mouseup", () => {
    isPainting = false;
    context.beginPath();
});
```

