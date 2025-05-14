## useAxios 커스텀 훅

- `useAxios`는 Axios를 사용해 HTTP 요청을 처리하는 커스텀 React Hook이다.
- Axios 인스턴스를 파라미터로 받을 수 있으며, 없을 경우 기본 Axios 인스턴스를 사용한다.
- `options.url`이 없으면 요청을 실행하지 않고 반환한다.
- 상태 관리는 `useState`로 `loading`, `error`, `data` 세 가지를 사용한다.
- 컴포넌트 마운트 시 `useEffect`에서 Axios 요청을 실행한다.
- 요청 성공 시 `data`에 결과를 저장하고 `loading`을 false로 변경한다.
- 요청 실패 시 `error`에 에러 객체를 저장하고 `loading`을 false로 변경한다.
- 재요청을 위한 `refetch` 함수가 포함되어 있으며, 내부적으로 상태를 변경해 `useEffect`를 다시 실행하게 만든다.
- `refetch`는 내부에서 `trigger` 값을 `Date.now()`로 갱신하여 의존성 배열 변경을 유도한다.
- 외부에서 `refetch()`를 호출하면 데이터를 다시 불러올 수 있다.

### 예시 코드

```jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

const useAxios = (options, axiosInstance = axios) => {
  const [state, setState] = useState({
    loading: true,
    error: null,
    data: null,
  });
  const [trigger, setTrigger] = useState(0);

  useEffect(() => {
    if (!options?.url) return;

    setState(prev => ({ ...prev, loading: true }));

    axiosInstance(options)
      .then(res => {
        setState({ loading: false, error: null, data: res.data });
      })
      .catch(err => {
        setState({ loading: false, error: err, data: null });
      });
  }, [trigger]);

  const refetch = () => {
    setTrigger(Date.now());
  };

  return { ...state, refetch };
};
