# Java Script 기초

## 브라우져 콘솔
- `console` : 코드 입력 및 실행, 결과 확인

## 기본 구조
- `app.js` : 실행 시킬 코드
- `index.html` : 코드가 실행되는 환경
- `style.css` : 스타일 지정

## const / let
- `const` : 상수 / 변경 불가능
- `let` : 변수 / 선언 후 변경 가능
- `var` : 현재는 사용되지 않음 / 변경 가능

## 이름 작성법
- `camelCase` 작성법 : `JS`
- `sneak_case` 작성법 : `Python`

```java
const a = 5;
const b = 2;
let myName = "polaris"

console.log(a * b)
console.log("hi my name is" + " " + myName)

myName = "Changed"
console.log("name is" + " " +  myName)

const caseA = false;
console.log(caseA)
const caseB = null;
console.log(caseB)
let caseC;
console.log(caseC)


// 10
// app.js:10 hi my name is polaris
// app.js:15 name is Changed
// app.js:18 false
// app.js:20 null
// app.js:22 undefined
```