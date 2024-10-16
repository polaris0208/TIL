## SQL 기능

### 연산

1. 복습
* 기본구조
 select
 from
 where
 
 * 주의점 - 문자 사용 시 '' 사용
 * 컬럼을 보기 쉽게 별명 설정이 필요 - 컬럼 별명

2. 연산
* 곱 - *, 나누기- /
_백분율 관련 계산은 소수를 사용_
* 함수 sum, avg, count, max, min-()를 이용해 범위 설정
_범위 설정에 유의_

3. 범주별 연산
* group by, order by
* 순서로 대체 가능 ex)group by 1
* 배열 기본값=오름차순, 내림차순=desc

### 데이터 가공
* replace(칼럼, 원본문자, 변경문자)
* substr(칼럼, 가져올 문자의 시작위치, 가져올 문자 수)
_숫자로 표현 ex)sunstr(adr, 1, 2)_
* concat(요소, 요소...)-합성 기능

### 조건문
* if(조건, 부합, 부합하지 않는 경우)
* case 여런 조건 설정
_case 
when 조건
then 결과
else 나머지
end 종료_