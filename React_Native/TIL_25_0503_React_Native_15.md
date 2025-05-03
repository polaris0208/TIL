# Paint To-Dos

## 핵심 개념 정리

- 기존 객체(`todos`)에 새로운 항목을 추가할 때 `Object.assign` 대신 **전개 연산자 (`...`)** 사용
- `ScrollView`를 사용하여 to-do 리스트를 스크롤 가능하게 만듦
- `Object.keys()`를 사용해 객체의 key 목록을 배열로 변환하고, `map()`으로 렌더링 반복
- 각 key에 대해 해당 to-do 항목을 렌더링하는 방식 적용
- React Native가 아닌 React JS 개념 기준으로 설명
- 스타일링을 통해 각 to-do 항목을 보기 좋게 표시 (배경색, 여백, 텍스트 색상 등)
- 다음 영상에서는 카테고리별 필터링 (work, travel) 및 디스크 저장 기능 예정


## 예시 코드

### 새로운 To-Do 추가하기

```js
const newTodos = {
  ...todos,
  [Date.now()]: { text: newToDoText, category: "work" }
};
```

---

### To-Do 목록 렌더링 (객체 기반)

```jsx
<ScrollView>
  {Object.keys(todos).map((key) => (
    <View key={key} style={styles.toDo}>
      <Text style={styles.toDoText}>{todos[key].text}</Text>
    </View>
  ))}
</ScrollView>
```


### 스타일 예시

```js
const styles = StyleSheet.create({
  toDo: {
    backgroundColor: theme.toDoBg,
    marginVertical: 10,
    paddingVertical: 20,
    paddingHorizontal: 40,
    borderRadius: 15,
  },
  toDoText: {
    color: "white",
    fontSize: 18,
    fontWeight: "500",
  }
});
```