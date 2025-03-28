# Form 개념 정리

## 입력값 검증 (Validation)
- 사용자 이름(Username)이 **비어있지 않도록** 확인 → 비어있으면 경고 메시지 출력
- 사용자 이름이 **15자 이하인지** 확인 → 초과하면 경고 메시지 출력
- `.length` 속성을 활용하여 문자열 길이 측정 가능

## JavaScript를 활용한 검증

```javascript
const value = loginInput.value;
if (value === "") {
    alert("이름을 입력해주세요");
} else if (value.length > 15) {
    alert("이름이 너무 깁니다");
}
```

## HTML의 기본 제공 기능 활용
- `<input>` 태그에 `required`와 `maxlength` 속성 추가 가능
- 브라우저가 자동으로 입력 검증 수행

## Form 요소와 제출 동작
- `<input>`을 `<form>` 내부에 배치하면 Enter 키를 눌렀을 때 자동으로 폼 제출됨
- `<button>` 클릭 시에도 자동으로 폼이 제출됨 → 페이지가 새로고침되는 문제 발생

## 폼 제출 방지 (페이지 새로고침 방지)

```javascript
form.addEventListener("submit", function(event) {
    event.preventDefault();  // 기본 동작(새로고침) 막기
    console.log("폼이 제출됨");
});
```

## 정리
- JavaScript와 HTML의 검증 기능을 조합하여 최적의 방법 사용
- 폼 제출 시 `event.preventDefault()`를 활용하여 새로고침 방지