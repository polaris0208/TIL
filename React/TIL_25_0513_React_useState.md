# useState 갸념 정리

## 객념 요약

* `useState`는 React에서 콘텐츠 상태(state)를 함수형 콘텐츠에서도 사용가능하게 해주는 훅(Hook)
* 기존 클래스 콘텐츠에서만 가능하던 state 관리 → 함수형 콘텐츠에서도 가능
* 가능성: 객보성 향상, 코드 간결화, 함수형 프로그래법 스택을 지향

## `useState` 기본 사용법

```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(1);

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);

  return (
    <div>
      <p>지금 값: {count}</p>
      <button onClick={increment}>증가</button>
      <button onClick={decrement}>감소</button>
    </div>
  );
}
```

### 설명

* `useState(1)` → 초기값은 1
* `count`: 현재 상태 값
* `setCount`: 상태를 변경하는 함수
* 이름은 자신의 필요에 따라 변경 가능 (ex. `[a, b] = useState(0)`)

## 구조 이해

```js
const [state, setState] = useState(초기값);
```

* 배열 구조 분할 합수 사용
* `state`: 현재 값
* `setState`: 상태 변경 함수

## 클래스 콘텐츠와의 비교

### 클래스 방식

```jsx
class Counter extends React.Component {
  state = {
    count: 1,
  };

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  decrement = () => {
    this.setState({ count: this.state.count - 1 });
  };

  render() {
    return (
      <div>
        <p>지금 값: {this.state.count}</p>
        <button onClick={this.increment}>증가</button>
        <button onClick={this.decrement}>감소</button>
      </div>
    );
  }
}
```

### 문제점

* `this`, `render()`, `setState()` 등 문법이 다양하고 복잡
* 코드 라인 수가 많아지고, 직관성 향후

## 기타 Hooks 소개 (간단 여러함)

* `useEffect`, `useContext`, `useReducer`, `useCallback`, `useMemo`, `useRef` 등
* 이 영상은 `useState`에 중점

## 마무리

* `useState`는 가장 기\uubcf8적이고 중요한 Hook
* 클래스 콘텐츠대비 **간단하고 직관적**
* 함수형 프로그래법 방식으로 코드의 자동화 가능
