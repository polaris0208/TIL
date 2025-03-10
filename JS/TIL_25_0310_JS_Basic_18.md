# To-Do 리스트 추가 기능

## 개념 정리

- `paintToDo` 함수는 새로운 할 일을 화면에 추가하는 역할을 한다.
- `handleToDoSubmit` 함수에서 입력 값을 받아 `paintToDo` 함수에 전달한다.
- `paintToDo` 함수는 `<li>` 요소를 생성하고, 내부에 `<span>`을 추가하여 할 일 내용을 표시한다.
- 생성한 `<li>` 요소를 기존 리스트(`<ul>` 등)에 추가하여 화면에 반영한다.
- 현재 코드의 한계점: 삭제 기능 없음, 새로고침 시 데이터 사라짐.

## 코드 예시

```javascript
// 할 일을 화면에 추가하는 함수
function paintToDo(newToDo) {
    // li 요소 생성
    const li = document.createElement("li");
    
    // span 요소 생성 및 할 일 텍스트 추가
    const span = document.createElement("span");
    span.innerText = newToDo;
    
    // li에 span 추가
    li.appendChild(span);
    
    // ul 또는 기존 리스트에 li 추가
    document.getElementById("toDoList").appendChild(li);
}

// 폼 제출 시 실행되는 함수
function handleToDoSubmit(event) {
    event.preventDefault(); // 기본 이벤트 방지
    const input = document.getElementById("toDoInput");
    const newToDo = input.value;
    input.value = ""; // 입력 필드 초기화
    paintToDo(newToDo); // 화면에 추가
}

// 이벤트 리스너 등록
document.getElementById("toDoForm").addEventListener("submit", handleToDoSubmit);
```

## 주요 흐름

- `paintToDo(newToDo)`: 새로운 `<li>`와 `<span>`을 만들어 리스트에 추가.
- `handleToDoSubmit(event)`: 사용자의 입력 값을 받아 `paintToDo` 호출.
- `event.preventDefault()`: 기본 폼 제출 동작을 막아 페이지 새로고침 방지.
- `input.value = "";`: 입력 필드 초기화.
- `document.getElementById("toDoList").appendChild(li);`: 리스트에 추가하여 화면에 표시.

