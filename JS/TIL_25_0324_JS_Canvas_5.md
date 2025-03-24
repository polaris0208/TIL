# 집 그리기 실습: `fill rect`와 삼각형 지붕 만들기

## `fill rect` 함수 사용법
- `fill rect`는 사각형을 그릴 때 사용되는 함수입니다. `fill`과 `rect`를 결합한 형태로, 내부적으로 `moveTo`와 `lineTo`가 사용됨
- `fill rect`를 사용할 때, 좌표와 크기(너비, 높이)를 지정하면 직사각형을 그림

```javascript
context.fillRect(200, 200, 50, 200);  // x: 200, y: 200, 너비: 50px, 높이: 200px
```

## 벽 그리기
- 첫 번째 벽을 `(200, 200)` 좌표에, 두 번째 벽을 `(400, 200)` 좌표에 그림

```javascript
context.fillRect(200, 200, 50, 200);  // 첫 번째 벽
context.fillRect(400, 200, 50, 200);  // 두 번째 벽
```

## 문 그리기
- 문을 그릴 때, `fill rect` 대신 `stroke rect`를 사용하여 테두리만 보이도록 설정
- `stroke rect`는 사각형의 테두리만 그리며, 내부는 채워지지 않음

```javascript
context.strokeRect(200, 300, 100, 200);  // 문
```

## 선 두께 조정
- 선의 두께는 `lineWidth` 속성을 사용하여 설정할 수 있습니다. 선의 두께를 2px로 설정
- `lineWidth`는 항상 스타일을 설정하기 전에 먼저 지정해야 합니다.

```javascript
context.lineWidth = 2;  // 선 두께 설정
context.strokeRect(200, 300, 100, 200);  // 문 테두리
```

## 천장 그리기
- 천장은 `fill rect`로 그리며, 200px 너비와 20px 높이로 설정

```javascript
context.fillRect(200, 200, 200, 20);  // 천장
```

## 삼각형 지붕 만들기
- 삼각형 지붕은 `moveTo`와 `lineTo`를 사용하여 좌표를 이동하고 선을 그림
- 삼각형의 세 점을 지정한 후, `stroke`나 `fill`을 사용하여 채우거나 테두리를 그림

```javascript
context.moveTo(200, 200);  // 시작 점
context.lineTo(325, 100);  // 삼각형의 꼭대기
context.lineTo(400, 200);  // 끝 점
context.closePath();  // 삼각형을 닫음
context.fill();  // 삼각형을 채움
```

