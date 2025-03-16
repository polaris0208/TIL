# 배열에서 요소 삭제

## 개념 정리

- 배열에서 특정 요소를 삭제할 때 원본 배열을 직접 수정하지 않고, **새로운 배열**을 생성하는 방식 사용
- `forEach`와 비슷하지만, 특정 조건을 만족하는 요소만 남기는 **`filter` 함수** 사용
- `filter` 함수는 콜백 함수를 인자로 받고, 각 요소를 평가하여 `true`인 요소만 새로운 배열에 포함

## `filter` 함수 기본 원리

- `filter`는 배열의 각 요소를 순회하면서 주어진 조건을 평가
- 조건이 `true`인 요소만 새로운 배열에 포함됨

### 모든 요소 유지

```javascript
const numbers = [1, 2, 3, 4];
const result = numbers.filter(() => true); // 모든 요소 유지
console.log(result); // [1, 2, 3, 4]
```

### 모든 요소 삭제

```javascript
const numbers = [1, 2, 3, 4];
const result = numbers.filter(() => false); // 모든 요소 삭제
console.log(result); // []
```

## 특정 요소 삭제

### 특정 숫자(3) 삭제

```javascript
const numbers = [1, 2, 3, 4];
const result = numbers.filter(num => num !== 3);
console.log(result); // [1, 2, 4]
```

### 특정 문자열("banana") 삭제

```javascript
const fruits = ["apple", "banana", "cherry"];
const result = fruits.filter(fruit => fruit !== "banana");
console.log(result); // ["apple", "cherry"]
```

## 조건 기반 필터링

### 1000 초과 숫자 삭제

```javascript
const numbers = [500, 1500, 2000, 300, 700];
const result = numbers.filter(num => num <= 1000);
console.log(result); // [500, 300, 700]
```

## `filter`를 활용한 To-Do 삭제

### 특정 `id`를 가진 할 일 삭제

```javascript
const todos = [
  { id: 1, text: "운동하기" },
  { id: 2, text: "공부하기" },
  { id: 3, text: "독서하기" }
];

const deleteId = 2;
const filteredTodos = todos.filter(todo => todo.id !== deleteId);
console.log(filteredTodos);
// [ { id: 1, text: "운동하기" }, { id: 3, text: "독서하기" } ]
```

### 특정 텍스트("공부하기")를 가진 할 일 삭제

```javascript
const deleteText = "공부하기";
const filteredTodos = todos.filter(todo => todo.text !== deleteText);
console.log(filteredTodos);
// [ { id: 1, text: "운동하기" }, { id: 3, text: "독서하기" } ]
