# JQuery
> **Java** 코드의 복잡성을 해결하기 위한 기능

## 개념
- **JavaScript**를 간결하고 쉽게 작성할 수 있도록 도와주는 라이브러리
- **JavaScript** 코드를 간단하게 작성
- **DOM(Document Object Model)** 요소를 쉽게 조작하거나 이벤트를 처리

## JQuery CDB
- **JQuery** 활성화
  - 웹 페이지에 **jQuery** 라이브러리 추가
- `head-script`
  - `src = "https://www.w3schools.com/jquery/jquery_get_started.asp"`

## JQuery 사용

### 요소 선택
- `$` 기호를 사용해 요소를 선택
  - `$('#id')`: 특정 **ID** 선택
  - `$('.class')`: 특정 클래스 선택
  - `$('태그')`: 특정 **HTML** 태그 선택

### 기본 조작
- `.text()` : 기존 텍스트를 변경
- `.append()` : 기존 내용 뒤에 새로운 내용 추가
- `.empty()` : 요소 내부의 모든 내용을 제거

### 기능 호출
- `body` : 실행 동작 
- `script` : **java** 함수 정의
- 스크립트에 정의된 함수를 불러와 동작 실행

```java
...button onclick="checkResult()"...
...
    function checkResult() {
      alert('확인')
    }
```

### 변수 호출
- `$('#선택자')`

```java
...id="q1"...
...
    function checkResult() {
      let word = 'test'
      $('#q1').text(word)
    }
```

### 리스트&딕셔너리 호출

```java
...div id="q1">
...
    function checkResult() {
      let fruits = ['사과','배','감','귤','수박']
      fruits.forEach(fruit => {
        let temp_html = `<p>${fruit}</p>`
        $('#q1').append(temp_html)
      });

      let people = [
          {'name':'서영', 'age':24},
          {'name':'현아', 'age':30},
          {'name':'영환', 'age':12},
          {'name':'서연', 'age':15},
          {'name':'지용', 'age':18},
          {'name':'예지', 'age':36}
          ]
      $('#q2').empty()
      people.forEach(person => {
              let name = person['name']
              let age = person['age']
              let temp_html = `<p>${name}은 ${age}살 입니다.</p>`
              $('#q2').append(temp_html)
            });

    }
```

### AJAX(비동기 JavaScript와 XML)
- 서버와 데이터를 주고받기

#### 기본 요청

```java
$.ajax({
    url: 'https://jsonplaceholder.typicode.com/posts', // 요청할 URL
    method: 'GET', // HTTP 요청 메서드
    success: function(data) {
        console.log(data); // 요청 성공 시 실행
    },
    error: function(error) {
        console.error(error); // 요청 실패 시 실행
    }
});
```

#### `$.get()`와 `$.post()`

```java
// GET 요청: 데이터를 서버에서 가져올 때
$.get('https://jsonplaceholder.typicode.com/posts', function(data) {
    console.log(data);
});

// POST 요청: 데이터를 서버에 보낼 때
$.post('https://jsonplaceholder.typicode.com/posts', { title: '새 글', body: '내용' }, function(data) {
    console.log(data);
});
```