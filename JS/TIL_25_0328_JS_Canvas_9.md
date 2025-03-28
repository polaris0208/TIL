# 캔버스 선 두께 조절하기

## 개념 정리

- HTML의 `<input type='range'>`를 사용하여 선 두께를 조절할 수 있음.
- JavaScript에서 `getElementById`를 이용해 입력 값을 가져옴.
- `addEventListener`를 활용하여 값 변경 시 이벤트 감지.
- `context.lineWidth`를 조절하여 선의 두께 변경.
- 기존 선과 새로운 선이 연결되지 않도록 `beginPath()`를 호출하여 새로운 경로 시작.
- `step` 속성을 활용하면 조절 단위를 세밀하게 설정 가능.

### JavaScript
```javascript
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const lineWidthInput = document.getElementById("line-width");

// 초기 선 두께 설정
ctx.lineWidth = lineWidthInput.value;

// 값 변경 이벤트 리스너 추가
lineWidthInput.addEventListener("input", (event) => {
    ctx.lineWidth = event.target.value;
    ctx.beginPath(); // 새로운 경로 시작
});
```

## 주요 개념 요약

- `min`, `max`, `value` 속성으로 범위 및 기본값 설정 가능.
- `step` 속성으로 조절 단위를 세밀하게 설정 가능.
- `addEventListener("input", callback)`을 사용하여 실시간 반영 가능.
- `ctx.beginPath()`를 호출하여 기존 선과 새로운 선이 연결되지 않도록 처리.

