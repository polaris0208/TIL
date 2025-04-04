## 캔버스에서 이미지 저장하는 방법 정리

#### 개요
- HTML5 캔버스에 그린 그림을 **이미지 파일(png)**로 저장할 수 있다.
- 저장 방식은 **`canvas.toDataURL()`**을 이용해 base64로 변환한 후, 가짜 `<a>` 태그를 만들어 클릭 이벤트를 발생시켜 다운로드를 트리거하는 방식이다.

---

### 주요 개념 정리

- `canvas.toDataURL()`
  - 캔버스의 현재 그림을 **Base64 형식의 이미지 데이터 URL**로 반환한다.
  - 기본 형식은 `image/png`, 필요 시 `image/jpeg`로 지정 가능.

- `document.createElement('a')`
  - 다운로드를 위한 **가짜 앵커 태그(a)** 생성.

- `a.href = [dataURL]`
  - 생성된 앵커 태그에 다운로드할 이미지 URL을 연결.

- `a.download = "파일이름.png"`
  - `download` 속성으로 저장할 **파일 이름** 지정.

- `a.click()`
  - 사용자가 클릭한 것처럼 **다운로드 동작을 자동 실행**.

---

### 코드 예시

```html
<canvas id="canvas" width="300" height="300" style="border:1px solid black;"></canvas>
<button id="save">Save Image</button>

<script>
  const canvas = document.getElementById("canvas");
  const saveButton = document.getElementById("save");

  saveButton.addEventListener("click", function onSaveClick() {
    // 1. 캔버스에서 이미지 데이터 추출 (base64 형식)
    const url = canvas.toDataURL("image/png");

    // 2. 다운로드용 링크 생성
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = "my_drawing.png";

    // 3. 다운로드 트리거
    anchor.click();
  });

  // 예시: 자동으로 사각형 그리기
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "skyblue";
  ctx.fillRect(50, 50, 100, 100);
</script>
```

---

### 요약

- 캔버스의 이미지를 파일로 저장하려면 `toDataURL()`을 사용해 base64 URL을 얻는다.
- 다운로드를 위해 `<a>` 태그를 동적으로 만들어 `href`와 `download` 속성을 설정한다.
- `click()` 메서드로 자동 클릭을 유도해 이미지가 저장되도록 한다.
