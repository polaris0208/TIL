# 캔버스(Canvas) 개념 정리 2

## fillRect와 Paths 개념
- `fillRect`는 캔버스에서 사각형을 그리는 단축 함수이다.
- 실제로는 먼저 선을 그리고, 이를 채우거나(`fill`), 테두리만 표시(`stroke`).

## 선을 그리고 채우는 과정
- 기본적인 과정:
  1. 선을 그림
  2. 채우거나(stroke, fill) 스타일 적용
- 여러 개의 선을 먼저 그리고 한 번에 채울 수도 있음.

```javascript
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

// 사각형의 경로 설정
ctx.beginPath();
ctx.rect(10, 10, 100, 100);
ctx.stroke(); // 테두리만 그림
```

## Paths의 개념
- Path(경로)는 캔버스에서 그려지는 도형들의 그룹을 의미함.
- 같은 Path 내에서는 스타일 변경 시 모든 도형이 영향을 받음.
- 개별 스타일을 적용하려면 `beginPath()`로 새로운 Path를 시작해야 함.

```javascript
ctx.fillStyle = "black";
ctx.fillRect(10, 10, 100, 100); // 검은색 사각형

ctx.fillStyle = "red";
ctx.fillRect(120, 10, 100, 100); // 이 사각형도 빨간색으로 바뀜 (같은 Path)
```

## beginPath()를 활용한 스타일 분리
- `beginPath()`를 사용하면 이전 Path와 독립적인 새로운 Path가 시작됨.
- 이를 활용하여 다른 스타일을 적용할 수 있음.

```javascript
ctx.fillStyle = "black";
ctx.fillRect(10, 10, 100, 100);

ctx.beginPath(); // 새로운 Path 시작
ctx.fillStyle = "red";
ctx.fillRect(120, 10, 100, 100); // 이제 이 사각형은 빨간색 유지
```

## 결론
- 캔버스에서 도형을 그릴 때는 Path 개념을 이해해야 한다.
- `beginPath()`를 사용하여 도형 그룹을 분리할 수 있다.
- 명확한 스타일링을 위해 Path의 상태를 관리하는 것이 중요하다.
