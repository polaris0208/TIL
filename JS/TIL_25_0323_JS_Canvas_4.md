# moveTo와 lineTo 함수 개념 정리

## 개념
- **moveTo(x, y)**: 
  - 브러시(또는 펜)를 지정된 좌표 (x, y)로 이동시킴
  - 선을 그리지 않음
  
- **lineTo(x, y)**: 
  - 현재 위치에서 지정된 좌표 (x, y)까지 선을 그리며 이동함
  
## 동작 순서
1. **moveTo**로 브러시를 시작 지점으로 이동
2. **lineTo**를 사용하여 선을 그리며 이동

```javascript
// 캔버스에서 선을 그리는 코드 예시

const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// 첫 번째 점으로 브러시를 이동
ctx.moveTo(50, 50);

// 두 번째 점까지 선을 그리기
ctx.lineTo(150, 50);  // 위쪽 수평선
ctx.stroke();          // 선을 그린 후 화면에 표시

// 새로운 점으로 브러시를 이동
ctx.moveTo(150, 50);

// 세 번째 점까지 선을 그리기
ctx.lineTo(150, 150);  // 오른쪽 세로선
ctx.stroke();

// 네 번째 점으로 브러시를 이동
ctx.moveTo(150, 150);

// 다섯 번째 점까지 선을 그리기
ctx.lineTo(50, 150);   // 아래쪽 수평선
ctx.stroke();

// 마지막 점으로 브러시를 이동
ctx.moveTo(50, 150);

// 첫 번째 점으로 돌아가 선을 그리기
ctx.lineTo(50, 50);    // 왼쪽 세로선
ctx.stroke();
```

## 설명
- `moveTo(50, 50)`로 브러시를 (50, 50)으로 이동시킴. 이때 선은 그려지지 않음
- `lineTo(150, 50)`으로 (50, 50)에서 (150, 50)까지 수평선이 그려짐
- `lineTo(150, 150)`, `lineTo(50, 150)`, `lineTo(50, 50)`을 사용하여 사각형을 완성

## 핵심 포인트
- `moveTo`는 브러시를 이동시키지만 선을 그리지 않음
- `lineTo`는 브러시를 이동시키면서 선을 그림
- 여러 번의 `moveTo`와 `lineTo`를 조합하여 복잡한 도형을 그림
