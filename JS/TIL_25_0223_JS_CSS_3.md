# JavaScript CSS 개념 정리

## `className`을 직접 변경하는 문제점
- `element.className = "new-class"`를 사용하면 기존 클래스가 사라짐
- `class="sexy-font clicked"` 상태에서 `className = "clicked"` 하면 `sexy-font` 사라짐

## `classList`를 활용한 클래스 제어
### `classList.contains()`
- 특정 클래스가 존재하는지 확인

```javascript
h1.classList.contains("clicked"); // true 또는 false 반환
```

### `classList.add()` & `classList.remove()`
- 특정 클래스를 추가 또는 제거

```javascript
h1.classList.add("clicked");   // 클릭된 클래스 추가
h1.classList.remove("clicked"); // 클릭된 클래스 제거
```

## `classList.toggle()`를 활용한 간단한 토글
- `toggle()`을 사용하면 특정 클래스가 있으면 제거, 없으면 추가

```javascript
h1.classList.toggle("clicked");
```

## `toggle()`을 사용한 코드 최적화
- 기존 코드

```javascript
if (h1.classList.contains("clicked")) {
    h1.classList.remove("clicked");
} else {
    h1.classList.add("clicked");
}
```

- `toggle()` 적용 후

```javascript
h1.classList.toggle("clicked");
```

## 결론
- `classList.toggle()`을 사용하면 간단한 UI 상태 변경을 쉽게 구현 가능
- 여러 줄의 코드를 단 한 줄로 줄일 수 있어 코드가 깔끔해짐
