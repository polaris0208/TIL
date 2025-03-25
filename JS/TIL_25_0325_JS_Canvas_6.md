## 캔버스에서 사람 그리기 프로젝트

### 개요
- `fillRect`을 사용하여 몸통, 팔, 다리를 그림
- `arc`를 사용하여 원을 그리고, 시작 및 종료 각도를 조절하여 반원 등 다양한 모양 생성
- `beginPath()`를 이용하여 새로운 경로를 시작하고, 색상을 개별적으로 조절
- 요소 위치 조정을 위해 x, y 좌표를 수정하며 배치 조정

### 주요 개념
#### 1. 사각형 그리기 (`fillRect`)

```javascript
context.fillRect(200, 200, 15, 100); // 팔
context.fillRect(350, 200, 15, 100); // 다른 팔
context.fillRect(260, 200, 60, 200); // 몸통
```

#### 2. 원 그리기 (`arc`)

```javascript
context.beginPath();
context.arc(250, 100, 50, 0, 2 * Math.PI);
context.fill();
```
- `arc(x, y, radius, startAngle, endAngle)`
- 원을 그릴 때 `startAngle = 0`, `endAngle = 2 * Math.PI`이면 완전한 원이 됨

#### 3. 부분 원 활용

```javascript
context.beginPath();
context.arc(250, 120, 8, Math.PI, 2 * Math.PI); // 웃는 입
context.stroke();
```
- `startAngle = Math.PI`부터 시작하면 반원이 됨

#### 4. 색상 변경 (`fillStyle`)

```javascript
context.beginPath();
context.fillStyle = "red";
context.arc(260, 120, 5, 0, 2 * Math.PI);
context.fill(); // 빨간색 눈
```
- `beginPath()`를 사용하지 않으면 기존 요소까지 영향을 받을 수 있음

### 정리
- `fillRect`로 사각형을 그려 신체를 구성
- `arc`를 사용하여 원과 반원을 만들어 얼굴 요소를 추가
- `beginPath()`를 활용하여 색상을 개별적으로 조절
- 위치 조정을 통해 균형 잡힌 그림을 생성

