## To-Do 항목 필터링 및 AsyncStorage로 저장하기

- **화면별 To-Do 필터링**
  - 각 To-Do 객체에는 `working: true/false` 속성이 있음
  - 현재 화면 모드(`working`)와 To-Do의 `working` 값을 비교하여 일치하는 항목만 렌더링
  - 예: 업무 화면에는 `working: true` 항목만 표시

- **AsyncStorage 설치**
  - `expo install @react-native-async-storage/async-storage` 명령어 사용
  - `expo install`은 현재 Expo SDK에 맞는 안정적인 버전을 설치

- **AsyncStorage 개념**
  - 브라우저의 localStorage와 유사
  - 문자열만 저장 가능
  - 비동기 함수이므로 `await` 필요

- **To-Do 저장 함수 구현**
  - 객체를 저장하려면 `JSON.stringify()`로 문자열 변환 필요
  - 저장 함수 예시:
    ```js
    const saveToDos = async (toDos) => {
      await AsyncStorage.setItem("toDos", JSON.stringify(toDos));
    };
    ```

- **To-Do 추가 시 저장 동기화**
  - 새로운 To-Do 추가 시 상태 업데이트 후 `saveToDos()` 호출
  - 예시:
    ```js
    const addToDo = (newToDo) => {
      const updatedToDos = {...toDos, [Date.now()]: newToDo};
      setToDos(updatedToDos);
      saveToDos(updatedToDos);
    };
    ```

- **To-Do 불러오기 함수 구현**
  - 앱 시작 시 저장된 To-Do 불러오기
  - 문자열 → 객체 변환: `JSON.parse()`
  - 예시:
    ```js
    const loadToDos = async () => {
      const data = await AsyncStorage.getItem("toDos");
      if (data) {
        setToDos(JSON.parse(data));
      }
    };
    ```

- **컴포넌트 마운트 시 불러오기**
  - `useEffect`를 사용해 첫 렌더링 시 `loadToDos()` 실행
    ```js
    useEffect(() => {
      loadToDos();
    }, []);
    ```

- **에러 처리 권장**
  - 실제 앱에서는 `try/catch`를 사용하여 저장/불러오기 오류에 대비
