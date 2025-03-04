# 인터벌(intervals) 개념 정리

## 개요
- 일정한 시간 간격마다 특정 작업을 실행하는 기능
- 자바스크립트에서 `setInterval`을 사용하여 구현
- 주로 실시간 데이터 갱신, 주기적인 서버 요청 등에 활용됨

## `setInterval` 개념
- 일정한 간격마다 지정한 함수 실행
- 두 개의 인자를 받음
  - 첫 번째 인자: 실행할 함수
  - 두 번째 인자: 실행 간격(밀리초 단위)

## 코드 예시

```javascript
// 5초마다 'Hello' 출력
function sayHello() {
    console.log("Hello");
}

setInterval(sayHello, 5000);
```

## 동작 과정
1. `sayHello` 함수 정의
2. `setInterval`을 이용해 `sayHello`를 5초마다 실행
3. 실행 후 콘솔에서 5초마다 "Hello" 출력됨

## 활용 예시
- 실시간 시계 구현
- 일정 주기마다 API 요청
- 자동 슬라이드 쇼 기능

## 참고 사항
- `setInterval`은 명시적으로 중지하지 않으면 계속 실행됨
- `clearInterval(intervalID)`를 사용하여 중지 가능

## 중지 코드 예시

```javascript
let intervalID = setInterval(sayHello, 5000);

// 15초 후 인터벌 중지
setTimeout(() => {
    clearInterval(intervalID);
    console.log("인터벌 중지");
}, 15000);
