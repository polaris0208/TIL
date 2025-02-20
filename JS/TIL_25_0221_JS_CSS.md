# JavaScript CSS 개념 정리
- `h1` 요소의 색상을 클릭할 때마다 변경

## 핵심 개념
1. **이벤트 리스너 제거** → 필요 없는 리스너 제거 후 `handleTitleClick` 함수에 집중
2. **색상 변경 로직**
   - `h1.style.color` 값을 확인하여 변경
   - `if-else` 문을 사용하여 색상 변경
3. **콘솔 로그 활용**
   - `console.log(h1.style.color)`로 색상 확인
4. **리팩토링**
   - 현재 색상을 `const currentColor`에 저장
   - `let newColor` 변수를 사용하여 변경될 색상 할당
   - `h1.style.color = newColor`로 최종 적용
5. **JS에서 CSS 조작에 대한 고민**
   - JavaScript에서 직접 스타일을 변경하는 것은 권장되지 않음
   - CSS 파일을 활용하는 방향으로 개선 예정

## 코드 예시

### 기본 코드

```javascript
const h1 = document.querySelector("h1");

function handleTitleClick() {
    if (h1.style.color === "blue") {
        h1.style.color = "tomato";
    } else {
        h1.style.color = "blue";
    }
}

h1.addEventListener("click", handleTitleClick);
```

### 리팩토링 코드

```javascript
const h1 = document.querySelector("h1");

function handleTitleClick() {
    const currentColor = h1.style.color;
    let newColor = currentColor === "blue" ? "tomato" : "blue";
    h1.style.color = newColor;
}

h1.addEventListener("click", handleTitleClick);
```

## 개선 방향
- **JS에서 CSS 직접 변경 대신 클래스 활용**
- **이벤트 흐름 정리**
  1. **요소 찾기** → `document.querySelector("h1")`
  2. **이벤트 리스너 등록** → `addEventListener("click", 함수명)`
  3. **이벤트 발생 시 스타일 변경** → `style.color` 변경
