# 기본 조건문

## if-else
- `isNaN`
  - `Not a Number` : 숫자가 아닌 경우 확인
- `prompt` 를 통해 입력된 내용이 숫자인지 확인
  - 숫자인 경우 출력
  - 아닌 경우 숫자 입력 안내

```js
const num = parseInt(prompt("Input number"))

if (isNaN(num)) {
  console.log("write number");
} else {
  console.log("number is " + num)
}
```

## else if
- `elif` 와 동일
- `&&` : `AND`
- `||` : `OR`
- 연산자를 이용하여 구간을 나눈 조건문 작성

```js
const age = parseInt(prompt("How old are you"))

if (isNaN(age) || age < 0) {
  console.log("write positive number");
} else if (age < 20) {
  console.log("You're too young");
} else if (age >= 20 && age < 50) {
  console.log("You can drink");
} else {
  console.log("You should exercise");
}
```