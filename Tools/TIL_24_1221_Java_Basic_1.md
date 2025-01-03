# Java 기초

## 기본

### 변수 선언
- `let` : 변수 선언
- `console.log()` : `console`에 변수 출력

```java
      let num = 20;
      console.log(num)
      num = 'Bob'
      console.log(num)
```

### 연산
- 변수 선언 후 연산
- 숫자 연산과 문자열 연산
- `console.log(first + a)`
  - 문자열 + 정수 조합 : 문자열 + 문자열로 출력

```java
      let a = 1
      let b = 2
      console.log(a + b)
      
      let first = 'Bob'
      let second = 'Lee'
      console.log(first + ' ' + second)   

      console.log(first + a)
```

### 리스트 & 딕셔너리

#### 리스트
- `[]`로 선언
- 인덱스 기능 : 순서가 존재
- `.push()` : 리스트 항목 추가
- `.length` : 길이

```java
    let list_1 = []
    let list_2 = [1, 2, 3, 'a', 'b', 'c']
    console.log(list_2[3])
    // a

    list_1.push('추가')
    console.log(list_1)
    // 추가
    console.log(list_1.length)
    // 1
```

#### 딕셔너리
- 키 : 벨류 조합

```java
    let dict_1 = {
      'name' : 'Alice',
      'age' : 7
    }
    console.log(dict_1['name'])
    // Alice

    dict_1['from'] = 'Wonderland'
    console.log(dict_1)
    // {name: 'Alice', age: 7, from: 'Wonderland'}
```

## 함수
- 특정 작업, 동작 수행

```java
    let email = 'test@mail.com'
    let result = email.split('@')
    console.log(result[0])
    // test
    console.log(result[1])
    // mail.com
```

### 함수 선언
- `function name(params) {return}`

```java
    function sum(num1, num2) {
        return num1 + num2
    }
    console.log(sum(1, 2))
    // 3
```

### 반복문
- `(let index = 0; index < 10; index++)`
  - `let index = 0;` : 변수 선언
  - `index < 10;` : 조건
  - `index++` : 후속 실행
- `{console.log(index)}` : 실행

```java
    for (let index = 0; index < 10; index++) {
      console.log(index)
    }
    // 0 ... 9
```

#### `foreach`
- 각 요소에 대한 실행

```java
    let nums = [1, 2, 3, 4, 5]
    nums.forEach(num => {
      console.log(num)
    });
    // 1 ... 5
```

### 조건문

```java
    let age = 30
    if (age>=20) {
      console.log('성인입니다.')
    } else {
      console.log('미성년자입니다.')      
    }
```

### 반복문 + 조건문

```java
    let ages = [93, 5, 16, 8, 9, 18]
    ages.forEach(age => {
      if (age >= 20) {
        console.log('성인입니다.')        
      } else {
        console.log('미성년자입니다.')          
      }
    });
```