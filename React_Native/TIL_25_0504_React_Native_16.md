## React Native에서 To-Do 앱 데이터 필터링

- 특정 화면에 맞는 to-do 항목만 필터링해서 보여줌  
  `working` 속성이 현재 모드와 일치하는 경우만 렌더링  

- 예시 코드
  ```js
  if (todo.working === isWorkingMode) {
    return <TodoItem ... />;
  }
  ```

- 앱 재실행 후에도 to-do 유지하기 위해 `AsyncStorage` 사용  
  Expo 환경에서는 `expo install @react-native-async-storage/async-storage`로 설치  

- `AsyncStorage`는 문자열만 저장 가능 → `JSON.stringify()`로 변환  
  ```js
  await AsyncStorage.setItem('todos', JSON.stringify(todos));
  ```

- 저장된 데이터를 불러올 때는 `JSON.parse()` 사용  
  ```js
  const jsonValue = await AsyncStorage.getItem('todos');
  const parsedTodos = JSON.parse(jsonValue);
  ```

- 앱 시작 시 데이터를 불러오기 위해 `useEffect`에서 `loadToDos()` 호출  
  ```js
  useEffect(() => {
    loadToDos();
  }, []);
  ```

- 전체 로직 요약  
  - to-do 추가 시 `saveToDos()` 호출  
  - `saveToDos()`는 to-do 리스트를 문자열로 변환 후 저장  
  - 앱 시작 시 `loadToDos()`로 저장된 데이터 불러와 상태로 복구  

- 에러 처리를 위해 실제 앱에서는 `try-catch` 블록 추가 권장  
  ```js
  try {
    const value = await AsyncStorage.getItem('todos');
    if (value !== null) {
      setToDos(JSON.parse(value));
    }
  } catch (e) {
    console.error('데이터 불러오기 실패', e);
  }
  ```
