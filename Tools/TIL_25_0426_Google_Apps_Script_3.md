# Google Apps Script 입력/조회 기능 만들기

## searchRecordMain() 함수

- 목적
  - `main` 시트에서 입력받은 정보로 다른 시트(특히 `면담기록`)를 검색하고 결과 표시

- 입력값 (main 시트 A2:E2)
  - 이름 (A2)
  - 분류 (B2) → 시트명
  - 시작일 (C2)
  - 종료일 (D2)
  - 면담 열 제목 (E2)

- 작업 흐름
  - 병합된 셀(A3:D3) 초기화
  - 이름 또는 분류 미입력 시 경고창 표시
  - 분류에 해당하는 시트 찾기 (없으면 경고창)
  - 이름에 해당하는 행 찾기 (없으면 "기록 없음" 출력)

- 분기 처리
  - 면담기록 시트
    - 면담 열(E2) 입력 필요
    - "전체" 선택 시 모든 면담 열 검색
    - 특정 열 선택 시 해당 열만 검색
    - 검색 결과 출력 (줄바꿈 포함)
  - 기타 시트
    - 시작일, 종료일 입력 필요
    - 날짜 포맷(yyMMdd)인 헤더만 검색
    - 시작일~종료일 범위 안의 데이터만 출력

- 보조 함수
  - parseHeaderToDate(header)
    - yyMMdd 포맷 문자열을 Date 객체로 변환

### 핵심 코드

```javascript
const nameRow = data.find(row => row[0] === name);
if (!nameRow) {
  mainSheet.getRange('A3:D3').setValue('해당 이름의 기록이 없습니다.');
  return;
}
```

```javascript
const headerDate = parseHeaderToDate(header);
if (headerDate >= startDate && headerDate <= endDate && cellValue !== "") {
  dateResults.push(`[${header}]\n${cellValue}`);
}
```

---

## addRecordToSheets() 함수

- 목적
  - `main` 시트에서 입력한 내용을 지정된 시트에 날짜별로 기록

- 입력값 (main 시트 A6:E7)
  - 이름 (A6)
  - 분류(시트명) (B6)
  - 시작일 (C6)
  - 종료일 (D6)
  - 면담 종류 또는 기록 종류 (E6)
  - 입력 내용 (A7, 병합셀)

- 작업 흐름
  - 날짜 범위(start~end) 생성
  - 시트 존재 여부 확인 (없으면 오류 발생)

- 분기 처리
  - 면담기록 시트
    - 면담 종류(열 제목) 필수
    - 이름이 없으면 새로 추가
    - 날짜별로 입력
    - 기존 기록이 있으면 줄바꿈 후 이어쓰기
  - 기타 일반 시트
    - 이름이 없으면 새로 추가
    - 날짜별로 입력
    - 기존 기록이 있으면 줄바꿈 후 이어쓰기

- 보조 함수
  - formatDateToHeader(dateStr)
    - Date를 yyMMdd 형식 문자열로 변환
  - getDateRange(start, end)
    - 시작일부터 종료일까지 Date 배열 생성

### 핵심 코드

```javascript
var rowIdx = names.indexOf(name) + 2;
if (rowIdx < 2) {
  rowIdx = sheet.getLastRow() + 1;
  sheet.getRange(rowIdx, nameCol).setValue(name);
}
```

```javascript
if (prev) {
  cell.setValue(prev + "\n" + content);
} else {
  cell.setValue(content);
}
```

---

# 정리 포인트

- main 시트는 검색 입력과 기록 입력의 중심
- 시트의 헤더는 yyMMdd 날짜 형식 또는 면담 종류 텍스트일 수 있음
- 이름이 없을 경우 자동 추가하는 구조
- 기존 내용이 있을 경우 줄바꿈 추가 작성 (\n)

