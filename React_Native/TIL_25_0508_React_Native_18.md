## 삭제 기능 구현

- **오류 처리 및 로딩 상태 고려**
  - `loadToDos` 함수에 `try-catch` 사용 권장
  - 로딩 상태를 위한 `loading` 상태(state) 추가 필요
  - 앱 시작 시 로딩 컴포넌트 표시하도록 구현

- **삭제 버튼 UI 구성**
  - 각 투두 항목 옆에 텍스트(X) 또는 아이콘 버튼 추가
  - `TouchableOpacity`로 클릭 가능한 영역 생성
  - `flexDirection: 'row'`, `justifyContent: 'space-between'`, `alignItems: 'center'` 설정으로 정렬

- **삭제 함수 구현**
  - `deleteToDo(key)` 함수 생성
  - key는 해당 투두의 생성 날짜 문자열
  - 기존 `toDos` 객체에서 해당 key를 제거한 새 객체 생성
  - 새 객체로 상태 업데이트 및 AsyncStorage에 저장

  ```js
  const deleteToDo = (key) => {
    const newToDos = { ...toDos };
    delete newToDos[key];
    setToDos(newToDos);
    saveToDos(newToDos);
  };
  ```

- **삭제 전 사용자 확인**
  - `Alert` API 사용 (Android와 iOS 모두 가능)
  - `Alert.alert()`에 제목, 메시지, 버튼 배열 설정
  - '취소'와 '확인' 버튼 제공
  - '확인' 버튼의 `onPress`에 `deleteToDo` 호출 연결

  ```js
  Alert.alert("Delete To-Do", "Are you sure?", [
    { text: "Cancel" },
    {
      text: "I'm sure",
      onPress: () => deleteToDo(key),
    },
  ]);
  ```

- **아이콘 변경**
  - 기본 이모지를 FontAwesome의 trash 아이콘으로 교체
  - `@expo/vector-icons`에서 `Fontisto` 사용
  - 적절한 크기와 색상 지정

  ```js
  import { Fontisto } from '@expo/vector-icons';

  <Fontisto name="trash" size={18} color="gray" />
  ```