# 이미지 업로드 및 처리

## 개요
- 파일 입력을 통해 이미지를 업로드하고, 이를 캔버스에 표시하는 기능 구현
- 브라우저의 보안 정책으로 인해 파일 시스템 접근이 제한됨
- 선택한 파일을 URL 객체로 변환하여 이미지 표시
- 이미지 로딩 후 캔버스에 렌더링하는 과정 설명

## 파일 입력 필드 생성
```html
<input type="file" id="file" accept="image/*">
```
- `accept="image/*"`를 사용하여 이미지 파일만 선택 가능하도록 제한

## JavaScript 코드
```javascript
const fileInput = document.getElementById('file');
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
document.body.appendChild(canvas);

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const url = URL.createObjectURL(file);
    const img = new Image();
    img.src = url;
    
    img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        URL.revokeObjectURL(url); // 메모리 해제
    };
});
```

## 코드 설명
- `fileInput.addEventListener('change', callback)` : 파일 선택 시 이벤트 감지
- `URL.createObjectURL(file)` : 선택한 파일을 브라우저 메모리에 로드하여 URL 생성
- `new Image().src = url` : 이미지 객체 생성 후 URL을 할당하여 로딩
- `img.onload` : 이미지가 로드되면 캔버스 크기 조정 후 `drawImage`로 그리기
- `URL.revokeObjectURL(url)` : 메모리 누수를 방지하기 위해 URL 해제

## 추가 기능
- 기존 이미지 제거 후 새로운 이미지 로딩
```javascript
fileInput.value = null;
```
- 업로드된 이미지를 다른 브라우저에서 사용할 수 없음 (보안 정책 적용)