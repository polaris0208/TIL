# Java Script Element

## `document`
- 브라우저를 통해 html과 소통
  - 콘솔에서 document 객체로 html 정보에 접근 가능

```js
document.title
// 'Document'

// 정보 수정도 가능
document.title = "Title Change"
// 'Title Change'

// 자바스크립트에 작성하면 html에 작성되어 있는 제목 변경 가능
document.title = "Title from JS";
// "Title from JS"
```

## Element

### `Id`로 조회
- `Id` 가 `title`인 경우 조회
- `dir` : `html` 객체 조회

```js
const title = document.getElementById("title");
console.dir(title);
// ...
// className: "class name"
// ...
// id: "title"
// inert: false
// innerHTML: "Header 1"
// innerText: "Header 1"
// ...
```

### `ClassName`
- `Class`명을 통한 조회
  - 중복이 있을 경우 배열

```js
const classes = document.getElementsByClassName("class_");
console.log(classes);
// 0: h1.class_
// 1: h1.class_
// 2: h1.class_
// 3: h1.class_
// 4: h1.class_
// length: 5
```

### `Tag`
- 특정 태그를 사용하는 `html` 객체 조회

```js
const tag_ = document.getElementsByTagName("h2");
console.log(tag_);
// HTMLCollection [h2]
```

## `querySelector`
- 특정 부분을 조회하고 싶을 때 사용

### `Id`
- `#` 뒤에 `Id` 지정

```js
const id_ = document.querySelector("#title");
console.log(id_)
// title
```

### `ClassName`
- `.` 뒤에 `Class`명 지정
- `querySelectorAll`: 전체 조회
  - 결과를 배열로 받음

```js
const class_ = document.querySelectorAll(".class_");
console.log(class_)
// NodeList(4) [div.class_, div.class_, div.class_, div.class_]
```

### 특정 `class`의 특정 `tag`
- 다른 내용을 가진 특정 태그를 조회하고 싶은 경우 사용

```js
const classH2 = document.querySelector(".class_ h2");
console.log(classH2)
// H2 Tag
```