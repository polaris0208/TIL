# o-Do 삭제 기능

## 목표
- To-Do 목록에서 특정 항목을 삭제할 수 있는 버튼 추가
- JavaScript의 이벤트 리스너 활용

## 구현 과정

### 버튼 추가하기
- `li` 요소 내부에 삭제 버튼 생성
- 버튼 클릭 시 이벤트 감지를 위해 `addEventListener` 설정

```javascript
const button = document.createElement("button");
button.innerText = "❌";  // 버튼에 X 표시 추가
li.appendChild(button);  // `li` 내부에 버튼 추가
```

### 클릭 이벤트 리스너 추가
- 버튼 클릭 시 `deleteToDo` 함수 실행

```javascript
button.addEventListener("click", deleteToDo);
```

### 클릭된 항목 삭제
- 클릭된 버튼의 부모 요소(`li`)를 찾아 제거
- `event.target.parentElement.remove()` 사용

```javascript
function deleteToDo(event) {
    const li = event.target.parentElement;  // 버튼의 부모 요소(li) 찾기
    li.remove();  // li 요소 삭제
}
```

## 정리
- 버튼을 생성하여 `li` 내부에 추가
- 버튼 클릭 시 이벤트 감지
- `event.target.parentElement.remove()`를 활용하여 해당 `li` 삭제