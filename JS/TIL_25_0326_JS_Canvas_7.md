# 캔버스에서 선 그리기

## 개념 정리

- **목표**: 사용자가 클릭하면 선을 그리는 간단한 드로잉 보드 구현
- **이벤트 리스너**: `canvas.addEventListener("click", onClick)`을 사용하여 클릭 감지
- **클릭 좌표 가져오기**: `event.offsetX`, `event.offsetY`를 사용하여 정확한 좌표 확인
- **선 그리기**: `context.lineTo(x, y)`를 사용하여 클릭한 위치까지 선을 그림
- **선 스타일 설정**: `context.lineWidth`와 `context.stroke()`로 선 스타일 지정
- **문제 해결**: 처음 클릭 시 선이 보이지 않는 문제를 `context.moveTo(x, y)`로 해결
- **마우스 이동 시 그리기**: `mousemove` 이벤트를 사용하여 클릭 없이도 선이 그려지도록 변경
- **랜덤 색상 적용**: 배열을 활용하여 매번 다른 색상으로 선을 그리도록 설정
- **경로 문제 해결**: `context.beginPath()`를 사용하여 이전 선의 색상이 변경되지 않도록 처리
- **추가 기능 아이디어**:
  - 클릭 시 원점 변경
  - 두 개의 색상 배열을 만들어 클릭할 때마다 색상 변경

## 코드 예시

```javascript
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
const colors = ["red", "blue", "green", "orange", "purple"];

canvas.addEventListener("mousemove", (event) => {
    const x = event.offsetX;
    const y = event.offsetY;
    const color = colors[Math.floor(Math.random() * colors.length)];
    
    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(x + 1, y + 1);
    context.strokeStyle = color;
    context.lineWidth = 2;
    context.stroke();
});
```

## 개선 아이디어
- 클릭할 때마다 원점 변경
- 색상 변경 트리거 추가
- 마우스 클릭 + 드래그 시에만 그림 그리기

