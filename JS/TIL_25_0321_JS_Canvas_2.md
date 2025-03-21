# 캔버스(Canvas) 개념 정리 2

## HTML에서 Canvas 요소 추가
- `<canvas>` 요소를 HTML에 추가하면 브라우저 화면에 픽셀을 그릴 수 있는 공간이 생성됨

## JavaScript에서 Canvas 접근
- JavaScript에서 `document.querySelector`를 사용해 `<canvas>` 요소를 선택함

  ```javascript
  const canvas = document.querySelector("#myCanvas");
  ```

## Context 가져오기
- `getContext("2d")` 메서드를 사용해 캔버스의 2D 컨텍스트를 가져옴
- 컨텍스트는 실제로 그림을 그리는 도구 역할을 함

  ```javascript
  const context = canvas.getContext("2d");
  ```

## Canvas 스타일 지정 (CSS)
- 캔버스 크기를 CSS로 지정 가능

## JavaScript에서 Canvas 크기 설정
- CSS 외에도 JavaScript에서 크기를 설정해야 함 (화질 개선 목적)

  ```javascript
  canvas.width = 800;
  canvas.height = 800;
  ```

## 캔버스 좌표 시스템
- 좌표 (0,0) 은 캔버스의 왼쪽 상단을 의미
- `x` 는 오른쪽 방향, `y` 는 아래쪽 방향으로 증가함

## 사각형 그리기 (fillRect)
- `fillRect(x, y, width, height)` 함수 사용
- (x, y) 는 사각형의 시작 위치, width 와 height 는 크기 지정

  ```javascript
  context.fillRect(50, 50, 100, 200);
  ```

  - (50,50) 위치에서 가로 100px, 세로 200px 크기의 사각형을 그림

## 색상 변경하기
- `fillStyle` 속성을 사용해 색상을 변경 가능
- 예제:

  ```javascript
  context.fillStyle = "red";
  context.fillRect(50, 50, 100, 200);
  ```

  - 빨간색으로 채워진 사각형을 그림

## 외곽선만 있는 사각형 그리기 (strokeRect)
- `strokeRect(x, y, width, height)` 함수 사용

  ```javascript
  context.strokeStyle = "blue";
  context.strokeRect(50, 50, 100, 200);
  ```

  - 파란색 외곽선을 가진 사각형을 그림

## 다음 단계
- 선, 원, 텍스트 등의 다양한 그리기 기능 학습
- 색상, 투명도, 패턴 적용법 익히기