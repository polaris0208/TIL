# 캔버스(Canvas) 개념 정리

## 캔버스란?
- `canvas`는 HTML 요소 중 하나로, 웹에서 그래픽을 그릴 수 있도록 지원하는 API
- JavaScript를 사용하여 동적으로 2D 및 3D 그래픽을 생성 가능
- 3D 그래픽은 WebGL을 활용하며, 본 문서에서는 2D 그래픽을 다룸

## 특징
- **하드웨어 가속 지원**: 빠른 그래픽 처리를 위해 GPU 활용 가능
- **HTML과의 관계**: `canvas` 요소는 HTML에서 단순한 컨테이너 역할, 실질적인 그래픽 처리는 JavaScript에서 수행
- **CSS 스타일링 불가**: `canvas` 내부 그래픽은 CSS로 스타일링할 수 없으며, 직접 JavaScript로 조작해야 함

## 기본 사용법

### 1. HTML에 `canvas` 요소 추가

### 2. JavaScript로 캔버스 컨텍스트 가져오기

```javascript
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d"); // 2D 그래픽을 위한 컨텍스트 가져오기
```

### 3. 도형 그리기 예제

```javascript
// 사각형 그리기
ctx.fillStyle = "blue"; // 채우기 색상 설정
ctx.fillRect(50, 50, 200, 100); // (x, y, width, height)
```

### 4. 선 그리기

```javascript
ctx.beginPath();
ctx.moveTo(50, 200);
ctx.lineTo(250, 300);
ctx.strokeStyle = "red";
ctx.lineWidth = 5;
ctx.stroke();
```

### 5. 원 그리기

```javascript
ctx.beginPath();
ctx.arc(150, 150, 50, 0, Math.PI * 2);
ctx.fillStyle = "green";
ctx.fill();
```

### 6. 애니메이션 구현

```javascript
let x = 0;
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // 캔버스 초기화
    ctx.fillStyle = "purple";
    ctx.fillRect(x, 100, 50, 50); // 움직이는 사각형
    x += 2;
    requestAnimationFrame(animate); // 프레임마다 실행
}
animate();
```

## 활용 예시
- 인터랙티브 웹 애플리케이션
- 데이터 시각화 (차트, 그래프)
- 게임 개발
- 애니메이션 및 그래픽 디자인

## 결론
- `canvas` API는 강력한 그래픽 기능을 제공하며, HTML과 JavaScript를 활용하여 다양한 시각적 표현 가능
- 기본 도형 그리기부터 애니메이션까지, 다양한 활용 방법 존재
- JavaScript의 수학적 개념과 결합하면 더욱 복잡한 그래픽을 구현 가능