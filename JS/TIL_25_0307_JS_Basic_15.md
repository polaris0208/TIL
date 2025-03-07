# 랜덤 명언 표시 기능 구현

## 개념 정리

- 명언 데이터를 배열(Array)로 관리하며, 각 요소는 `quote`(문장)와 `author`(저자) 속성을 가진 객체(Object)로 구성됨.
- HTML에 명언을 표시할 `div`와 `span` 태그를 생성하여 활용.
- JavaScript에서 `document.querySelector()`를 사용해 HTML 요소를 선택하고 데이터를 적용.
- `Math.random()`과 `Math.floor()`를 조합하여 배열에서 랜덤한 요소를 선택.
- `quotes.length`를 활용해 동적으로 배열 길이를 반영하여 코드 유지보수를 용이하게 함.


## 명언 데이터 준비 (`quotes.js`)

```javascript
const quotes = [
    { quote: "The only limit to our realization of tomorrow is our doubts of today.", author: "Franklin D. Roosevelt" },
    { quote: "Do what you can, with what you have, where you are.", author: "Theodore Roosevelt" },
    { quote: "Life is what happens when you're busy making other plans.", author: "John Lennon" },
    { quote: "The way to get started is to quit talking and begin doing.", author: "Walt Disney" },
    { quote: "Don’t watch the clock; do what it does. Keep going.", author: "Sam Levenson" }
];
```

## 랜덤 명언 표시 (`script.js`)

```javascript
// 랜덤 숫자 생성 함수
function getRandomIndex(max) {
    return Math.floor(Math.random() * max);
}

// 명언 업데이트 함수
function displayRandomQuote() {
    const randomIndex = getRandomIndex(quotes.length);
    const todayQuote = quotes[randomIndex];
    
    document.getElementById("quote-text").innerText = todayQuote.quote;
    document.getElementById("quote-author").innerText = `- ${todayQuote.author}`;
}

// 페이지 로드 시 실행
displayRandomQuote();
```

## 핵심 요약

- **배열 객체 활용**: 명언 데이터는 `quote`와 `author` 속성을 가진 객체 배열로 저장.
- **HTML 요소 조작**: `document.getElementById()`로 요소를 가져와 `innerText`를 변경.
- **랜덤 요소 선택**: `Math.random()`과 `Math.floor()`를 사용하여 배열에서 무작위 요소를 선택.
- **자동 실행**: `displayRandomQuote()` 함수를 페이지 로드시 실행하여 명언을 표시.
