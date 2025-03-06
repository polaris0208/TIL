## padStart 개념 정리

### 개요
- `padStart`는 JavaScript의 문자열 메서드로, 특정 길이에 도달할 때까지 문자열 앞에 지정된 문자를 추가함
- 주로 숫자를 문자열로 변환한 후, 앞자리에 `0`을 추가할 때 사용됨 (예: 시간 표시 형식)

### 사용법
- `targetLength`: 목표 문자열 길이
- `padString`: 앞에 추가할 문자열 (기본값: 공백 문자)

```javascript
string.padStart(targetLength, padString)
```

### 예제
#### 1. 숫자를 두 자리로 만들기

```javascript
let num = "5";
console.log(num.padStart(2, "0")); // "05"
```

#### 2. 시간 표시 형식 만들기

```javascript
function formatTimeUnit(unit) {
    return String(unit).padStart(2, "0");
}

let hours = 9;
let minutes = 3;
let seconds = 7;

console.log(`${formatTimeUnit(hours)}:${formatTimeUnit(minutes)}:${formatTimeUnit(seconds)}`);
// 출력: "09:03:07"
```

#### 3. 문자열을 특정 길이로 맞추기

```javascript
let text = "hello";
console.log(text.padStart(10, "*")); // "*****hello"
```

### 주의사항
- `padStart`는 문자열에서만 사용 가능하며, 숫자에 직접 적용할 수 없음 → 숫자는 `String()`을 사용하여 문자열로 변환 후 적용

```javascript
let num = 5;
console.log(String(num).padStart(2, "0")); // "05"
```

- `targetLength`가 원래 문자열 길이보다 작거나 같으면 `padStart`는 아무 동작도 하지 않음

```javascript
console.log("123".padStart(3, "0")); // "123" (변화 없음)
```

### 관련 메서드
- `padEnd(targetLength, padString)`: 문자열 뒤에 `padString`을 추가하여 `targetLength`를 맞춤

```javascript
console.log("hello".padEnd(10, "*")); // "hello*****"
```

