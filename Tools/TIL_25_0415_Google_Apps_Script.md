# Google Apps Script
> ßonEdit 이벤트로 자동 데이터 입력 및 기록하기

## 목적
- 시트2에 입력된 정보(이름, 내용, 열 이름)를 바탕으로
- 시트1의 특정 위치에 내용을 자동 기록
- 이름이나 열이 없을 경우 새로 추가
- 입력 후 입력란 자동 초기화


## 시트 구조

### 시트1 (기록 대상)
- 1행: 열 제목 (헤더)
- C열: 이름이 위치하는 열

### 시트2 (입력 시트)
- M4:M5 → 이름 입력
- N4:N5 → 내용 입력
- O4:O5 → 열 이름 입력


## 사용된 주요 기능

### onEdit(e)
- 사용자가 시트를 편집할 때마다 호출됨
- 편집된 시트가 `시트2`가 아니면 종료

### 입력값 가져오기
```javascript
const name = sheet.getRange("M4:M5").getValue();
const content = sheet.getRange("N4:N5").getValue();
const columnName = sheet.getRange("O4:O5").getValue();
```
- 각각 이름, 내용, 열 제목을 가져옴
- 하나라도 비어 있으면 함수 종료

### 대상 시트 가져오기
```javascript
const targetSheet = ss.getSheetByName("시트1");
```
- 기록할 시트가 존재하는지 확인
- 없으면 로그 출력 후 종료

### 헤더(1행) 정보 가져오기 및 열 인덱스 구하기
```javascript
const headers = targetSheet.getRange(1, 1, 1, lastCol).getValues()[0];
let colIndex = headers.indexOf(columnName) + 1;
```
- 시트1의 첫 번째 행(헤더)을 배열로 가져옴
- columnName이 없으면 새로 열 생성

### 열이 없을 경우 새로 생성
```javascript
if (colIndex === 0) {
  colIndex = headers.length + 1;
  targetSheet.getRange(1, colIndex).setValue(columnName);
}
```
- 기존 열에 해당 columnName이 없을 경우
- 헤더 마지막에 새로운 열을 추가

### 이름 목록 가져오기 및 행 인덱스 구하기
```javascript
const names = targetSheet.getRange(2, 3, lastRow - 1, 1).getValues().flat();
let rowIndex = names.indexOf(name) + 2;
```
- C열에 있는 이름 목록을 가져옴
- 해당 이름이 없다면 새로 추가할 준비

### 이름이 없을 경우 새로 추가
```javascript
if (rowIndex === 1) {
  rowIndex = targetSheet.getLastRow() + 1;
  targetSheet.getRange(rowIndex, 3).setValue(name);
}
```
- 이름이 목록에 없을 경우
- 다음 빈 행의 C열에 이름 입력

### 기존 값과 합쳐서 기록
```javascript
const oldValue = cell.getValue();
const newValue = oldValue ? oldValue + '\n' + content : content;
cell.setValue(newValue);
```
- 기존 셀 값이 있으면 줄바꿈 후 이어 붙임
- 없으면 그대로 입력

### 입력 영역 초기화
```javascript
sheet.getRange("M4:O5").clearContent();
```
- 입력 후 입력란 초기화
- 다음 입력을 위한 준비

---

## 전체 코드

```javascript
function onEdit(e) {
  try {
    const ss = e.source;
    const sheet = ss.getActiveSheet();
    if (sheet.getName() !== "시트2") return;

    const name = sheet.getRange("M4:M5").getValue();
    const content = sheet.getRange("N4:N5").getValue();
    const columnName = sheet.getRange("O4:O5").getValue();

    if (!name || !content || !columnName) return;

    const targetSheet = ss.getSheetByName("시트1");
    if (!targetSheet) {
      Logger.log("시트1을 찾을 수 없습니다.");
      return;
    }

    const lastCol = Math.max(1, targetSheet.getLastColumn());
    const headers = targetSheet.getRange(1, 1, 1, lastCol).getValues()[0];

    let colIndex = headers.indexOf(columnName) + 1;
    if (colIndex === 0) {
      colIndex = headers.length + 1;
      targetSheet.getRange(1, colIndex).setValue(columnName);
    }

    const lastRow = Math.max(2, targetSheet.getLastRow());
    const names = targetSheet.getRange(2, 3, lastRow - 1, 1).getValues().flat();

    let rowIndex = names.indexOf(name) + 2;
    if (rowIndex === 1) {
      rowIndex = targetSheet.getLastRow() + 1;
      targetSheet.getRange(rowIndex, 3).setValue(name);
    }

    const cell = targetSheet.getRange(rowIndex, colIndex);
    const oldValue = cell.getValue();
    const newValue = oldValue ? oldValue + '\n' + content : content;
    cell.setValue(newValue);

    sheet.getRange("M4:O5").clearContent();

  } catch (error) {
    Logger.log("오류 발생: " + error);
  }
}
```


## 작동 방식 요약

- 시트2에 이름, 내용, 열 이름 입력
- 셀 수정 시 자동 실행
- 시트1에 해당 위치에 내용 기록
- 기존 값이 있다면 줄바꿈 후 누적
- 입력 후 시트2 입력란 초기화