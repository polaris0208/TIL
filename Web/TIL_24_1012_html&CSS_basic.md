## html & CSS 기초
>html 은 뼈대
CSS는 꾸미기 기능
java script는 동작

### vscode 사용 tip
```
html 작성에서 ! 하면 자동완성
h1 - tap - <h1></h1> 자동완성
command / 주석처리
추가기능 open in browser 설치
```
### html 기본구조
```
기본 구조 <head> - <body> 
<head> 속성 등 실제로 보여지지 않는 내용 등
<body> 실제로 보여지는 것
```
#### 기본 요소 tags
* hr, div, span 의 용도구분에 주의
```html
<> = tag 
<h1> 제목
<h2> 소제목 h3~6 등등 기능이 갈리
<hr> horizontal rule ; 수평 구분, 주제 구분, 장면 전환 / 하위 콘텐츠를 갖지 않음; </hr>을 사용하지 않음
<div> 구역을 나눔
<span> 포장 기능, 특정 문자들에 style을 정해줄 떄 사용 <div>와 기능 자체는 유사하나 용도가 다르기 떄문에 구분이 필요
<a> href, 하이퍼링크에 사용
<img> 이미지
<input> input, type 설정 필요
<button> 버튼
<textarea> 더 많은 텍스트
<dl> description list  정의 목록 태그
<dt> desctiption term  용어 태그 key값
<dd> description data 용어의 정의 태그 value값
<dfn> 정의 태그, <dt>와 유사한 기능, 화면상에는 기울임꼴로 나타남
<p> 문단
<ul> Unordered list 비정렬 목록
<ol> ordered list
<li> list item 목록의 항목
```
#### CSS
#### style
* css = html을 꾸며줌
```
선택자 {속성: 속성값; , 속성: 속성값;}
type(해당타입) 타입명
class(여러 요소) .클래스
id(유일한 요소) #아이디
```
```
  <style>
    /*css*/ .mytitle { color : red; font-size: 40px; }
            #id { color : blue; }
            .mybtn { color : green; background-color: white; font-size: 12px;}
            .mytxt { color : purple;}

  </style>
```
* 선택자의 종류는 매우 다양
* 포함관계가 있는 경우가 있음
tags의 하위 관계(포함 관계) - 부모-자식 등
부모-자식 선택자는 css를 공유(전체는 아님)
* 선택자 간의 우선 순위가 달라질 수 있음
선택자 개념: https://coding23213.tistory.com/15
```py
* 전체 선택자 *
* 하위 선택자 - 요소 내부의 모든 요소 / 현재 요소의 선택자(공백)하위 요소의 선택자
* 자식 선택자 - 요소 내부의 요소(하위의 하위 요소는 해당하지 않음) 현재 > 자식
* 인접 선택자 - 현재 요소 뒤에 나오는 요소 / 현재 + 인접
* 형제 선택자 - 같은 계층에 있는 요소 / 현재 ~ 형제
* 그룹 선택자 - 여러 요소들을 묶어서 / 요소1, 요소2, 
```
#### flex
* html은 박스형태 
* block 1줄 전체를 차지 - 위에서 아래로
* inline 글자같은 것들, 자신의 크기 만큼만 차지 - 가로로 배치
```
display : flex 작성 기준이 위-아래 에서 좌-우로 변경
justify-content: center 중앙 정렬(좌우폭)
align-items: center 중앙 정렬 (상하폭)
개발자 도구- 하단 - 스타일; 다른 설정 확인 가능
```