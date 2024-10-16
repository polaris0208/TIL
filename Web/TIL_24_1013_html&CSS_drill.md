## 간단한 웹사이트 제작

> 웹사이트 기본구조
style 작성법
구글폰트 적용법
bootstrap 활용법

### 웹사이트 기본구조
* nav, footer 부분은 대부분 고정적인 형태(메뉴, 연락처)
* main 부분은 여러 형태 가능
* 배경 적용할 경우 최상위 계층으로 적용
* div.background-banner 형식으로 태그 자동완성
* alt 누르고 클릭 - 다중 커서
```html
<head> 웹사이트 속성
 <meta> <title>, <style> 포함 
</head> 
<body> 웹사이트 내용
 <div class='background-banner'>
	<nav> 상단 바 부분
    <main> 주 콘텐츠 부분
    <footer> 하단부 
 </div>
 </body>
```

### style 작성법
* justify-content: space-between;
	공간을 두고 정렬 - 두개면 양끝 세개면 양끝과 가운데
* margin은 요소 사이거리
* padding은 요소와 요소의 테두리 사이 거리
	padding: 20px 0;
* viewport heighy 100은 영역(사각형) 100% 만큼 내린다
	height: 100vh;
* css 파일을 만들어 style 양식을 따로 분리
     link.css로 자동완성 - 코드 작성 후 alt+shift+f 자동정렬
     
```html
<link rel="stylesheet" href="style.css">
```

### 구글폰트 적용
* 구글폰트- code로 받기  https://fonts.google.com/
* style 태그 내부에 작성
```html
<style>
	@import url('https://fonts.googleapis.com/css2?family=Qwitcher+Grypen:wght@400;
    700&family=Sixtyfour+Convergence&display=swap');
    * {
      font-family: "Qwitcher Grypen", cursive;
      font-weight: 400;
      font-style: normal;
    }
</style>
```

### bootscrap 활용
* bootscrap에서 요소들을 붙여넣기 후 수정하여 사용
* 별도의 style 작성 없이 class명에 스타일 적용 가능
  d-flex justify-content-between
* bootscrap class명은 별도의 양식 사용 
	mx-auto 가로 가운데 정렬 w-75 가로 길이를 75%
* https://inpa.tistory.com/entry/BootStrap5-📚-부트스트랩-클래스-이름-정리


```html
<nav class="navbar border-bottom border-body d-flex justify-content-between" data-bs-theme="dark">
```
