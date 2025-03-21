# JavaScript 기본 문법 정리

## 변수 선언

```javascript
var x = 10; // 재선언 가능
let y = 20; // 재선언 불가능
const z = 30; // 재할당 불가능
```

## 데이터 타입

```javascript
let num = 10;       // 숫자 
let str = "Hello"; // 문자열 
let bool = true;    // 불리언
let obj = { name: "Alice", age: 25 }; // 객체 
let arr = [1, 2, 3]; // 배열
let undef;          // undefined
let nul = null;     // null
```

## 조건문

```javascript
let age = 20;
if (age >= 20) {
    console.log("성인입니다.");
} else {
    console.log("미성년자입니다.");
}
```

## 반복문

```javascript
for (let i = 0; i < 5; i++) {
    console.log("Hello");
}

let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
```

## 함수

```javascript
function add(a, b) {
    return a + b;
}
console.log(add(2, 3)); // 5

const multiply = (a, b) => a * b;
console.log(multiply(3, 4)); // 12
```

## 객체

```javascript
let person = {
    name: "Alice",
    age: 25,
    greet: function() {
        console.log("Hello, " + this.name);
    }
};
person.greet(); 

// Hello, Alice
```

## 배열

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[0]); 
// Apple
fruits.push("Mango"); // 배열에 추가
fruits.pop(); // 마지막 요소 제거
```

##  기타

```javascript
let name = "Tom";
console.log(`안녕하세요, ${name}!`);

// 스프레드 연산자
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];
console.log(arr2);
```