# 시간 지연 및 날짜 다루기

## setTimeout과 setInterval

- `setTimeout`: 일정 시간이 지난 후 **한 번만** 함수를 실행
- `setInterval`: 일정 시간마다 **반복적으로** 함수를 실행

```javascript
setTimeout(() => {
    console.log("5초 후 실행됨");
}, 5000);
```

```javascript
setInterval(() => {
    console.log("1초마다 실행됨");
}, 1000);
```

## JavaScript의 Date 객체

- `Date` 객체를 사용하여 현재 날짜 및 시간 정보를 가져올 수 있음
- 주요 메서드:
  - `getDate()`: 날짜 (일)
  - `getDay()`: 요일 (0: 일요일 ~ 6: 토요일)
  - `getFullYear()`: 연도
  - `getHours()`: 시간
  - `getMinutes()`: 분
  - `getSeconds()`: 초

```javascript
const now = new Date();
console.log(now.getFullYear()); // 2021
console.log(now.getHours()); // 현재 시간
console.log(now.getMinutes()); // 현재 분
console.log(now.getSeconds()); // 현재 초
```

## 실시간 시계 만들기

1. `setInterval`을 사용하여 1초마다 현재 시간을 가져오기
2. `Date` 객체의 `getHours()`, `getMinutes()`, `getSeconds()` 메서드를 활용
3. 시간 표시 형식을 `00:00:00` 형태로 포맷팅
4. `innerText`를 사용하여 웹 페이지에 표시

```javascript
function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    document.getElementById("clock").innerText = `${hours}:${minutes}:${seconds}`;
}

// 최초 실행 후 1초마다 갱신
updateClock();
setInterval(updateClock, 1000);
```

## 시계 즉시 업데이트 문제 해결

- `setInterval`만 사용할 경우, 웹페이지 로드 후 1초 대기해야 시간이 표시됨
- 해결 방법: `setInterval`을 실행하기 전에 한 번 `updateClock()`을 호출

```javascript
updateClock();
setInterval(updateClock, 1000);
```

## 시각 포맷팅 (한 자리 숫자 앞에 0 붙이기)

- `padStart(2, '0')` 사용하여 한 자리 숫자를 두 자리로 변환

```javascript
const num = 5;
console.log(String(num).padStart(2, '0')); // "05"
```

## 요약

- `setTimeout`: 일정 시간 후 **한 번만** 실행
- `setInterval`: 일정 시간마다 **반복적으로** 실행
- `Date` 객체를 사용하여 현재 날짜 및 시간 가져오기
- 실시간 시계를 만들 때 `setInterval`을 사용하며, 첫 실행 시 `updateClock()`을 호출
- `padStart(2, '0')`로 숫자를 2자리로 맞추어 가독성 개선

