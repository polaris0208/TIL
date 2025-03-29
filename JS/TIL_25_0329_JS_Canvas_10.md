# 색상 변경 기능 구현

## 개념 정리

- HTML의 `<input type="color">` 요소를 사용하면 사용자가 원하는 색상을 선택할 수 있음.
- JavaScript를 이용하여 선택된 색상을 캔버스의 선(stroke) 또는 도형 채우기(fill) 색상으로 변경 가능.
- `addEventListener('change', function)`을 사용하여 사용자가 색상을 변경할 때 자동으로 반영되도록 설정.
- `strokeStyle`은 선의 색상을, `fillStyle`은 도형 내부의 색상을 지정하는 데 사용됨.

## 코드 예시

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>색상 변경 기능</title>
</head>
<body>
    <input type="color" id="colorPicker">
    <canvas id="canvas" width="500" height="500" style="border:1px solid black;"></canvas>
    
    <script>
        const canvas = document.getElementById("canvas");
        const ctx = canvas.getContext("2d");
        const colorPicker = document.getElementById("colorPicker");
        
        // 초기 색상 설정
        ctx.strokeStyle = "black";
        ctx.fillStyle = "black";

        // 색상 변경 이벤트 리스너 추가
        colorPicker.addEventListener("change", (event) => {
            const selectedColor = event.target.value;
            ctx.strokeStyle = selectedColor;
            ctx.fillStyle = selectedColor;
        });
        
        // 예제: 사각형 그리기
        ctx.fillRect(50, 50, 100, 100); // 색상이 변경될 경우 적용됨
    </script>
</body>
</html>
```